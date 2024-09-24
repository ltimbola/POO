#%%
from datetime import datetime
import pytz

# Define a class called ContaCorrente
class ContaCorrente:
    
    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('America/Sao_Paulo')
        hora_BR = datetime.now(fuso_BR)
        return hora_BR.strftime('%d/%m/%Y %H:%M:%S')    
    
    def __init__(self, nome, cpf, agencia, numero_conta):
        self.nome = nome
        self.cpf = cpf
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.saldo = 0
        self.limite = None
        self. transacoes = []
        
    def consultar_saldo(self):
        print(f'Saldo: R$ {self.saldo:,.2f}')

    def alterar_nome_correntista(self, novo_nome):
        self.nome_correntista = novo_nome

    def depositar(self, valor):
        self.saldo += valor
        self.transacoes.append((f'Depósito de R$ {valor:,.2f}', f'Saldo de R$ {self.saldo:,.2f}', ContaCorrente._data_hora()))
        print(f'Depósito efetuado com sucesso, seu valor é de R$ {self.saldo:,.2f}')
        
    # Function to set the limit of the account(method private)     
    def _limite_da_conta(self):
        self.limite = -1000
        return self.limite
    
    # Function to check the limit of the account
    def consultar_limite(self):
        print(f'O limite da conta é de R$ {self.limite:,.2f}')

    def resgatar(self, valor):
        if self.saldo - valor < self._limite_da_conta():
            print('Saldo insuficiente')
            self.consultar_saldo()
            
        else:
            self.saldo -= valor
            self.transacoes.append((f'Resgate de R$ {-valor:,.2f}', f'Saldo de R$ {self.saldo:,.2f}', ContaCorrente._data_hora()))
            print('Resgate efetuado com sucesso')
            self.consultar_saldo()
            

    def transferir(self, conta_destino, valor):
        if self.sacar(valor):
            conta_destino.depositar(valor)
            return True
        else:
            return False
        
    def consulta_extrato(self):
        print('Extrato da conta')
        for transacao in self.transacoes:
            print(transacao)
            

    # def __str__(self):
    #     return f'Conta {self.numero}, Correntista: {self.nome_correntista}, Saldo: {self.saldo}'
    
# Test the class    
__name__ = '__main__'
conta_leonardo = ContaCorrente('Leonardo', '229.583.958-04', '1234', '030462')
conta_leonardo.depositar(1000)
conta_leonardo.resgatar(1500)
conta_leonardo.consulta_extrato()





