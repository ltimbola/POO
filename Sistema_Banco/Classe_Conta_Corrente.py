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
        self._nome = nome
        self._cpf = cpf
        self.__agencia = agencia
        self.__numero_conta = numero_conta
        self._saldo = 0
        self._limite = None
        self._transacoes = []
        self.cartoes = []

    def consultar_numero_conta(self):
        return self.__numero_conta
        
    def consultar_saldo(self):
        print(f'O saldo da conta {self.__numero_conta} é: R$ {self._saldo:,.2f}')

    def alterar_nome_correntista(self, novo_nome):
        self._nome = novo_nome

    def depositar(self, valor):
        self._saldo += valor
        self._transacoes.append((f'Depósito de R$ {valor:,.2f}', f'Saldo de R$ {self._saldo:,.2f}', ContaCorrente._data_hora()))
        print(f'Depósito de R$ {valor:,.2f} efetuado com sucesso na conta {self.__numero_conta}')
        self.consultar_saldo()

    # Function to set the limit of the account(method private)     
    def _limite_da_conta(self):
        self._limite = -1000
        return self._limite
    
    # Function to check the limit of the account
    def consultar_limite(self):
        print(f'O limite da conta {self.__numero_conta} é de R$ {self._limite:,.2f}')

    def resgatar(self, valor):
        if self._saldo - valor < self._limite_da_conta():
            print(f'Saldo insuficiente na conta {self.__numero_conta}')
            self.consultar_saldo()
            
        else:
            self._saldo -= valor
            self._transacoes.append((f'Resgate de R$ {-valor:,.2f}', f'Saldo de R$ {self._saldo:,.2f}', ContaCorrente._data_hora()))
            print(f'Resgate de R$ {-valor:,.2f} efetuado com sucesso na conta {self.__numero_conta}')
            self.consultar_saldo()
            

    def transferir(self, valor, conta_destino):
        print('Transferência de valores:')
        self.resgatar(valor)
        conta_destino.depositar(valor)
        print(f'Transferência efetuada com sucesso para a conta {conta_destino.__numero_conta}')
            
        # else:
        #     print(f'Transferência não efetuada para a conta {conta_destino._numero_conta}')
        
    def consulta_extrato(self):
        print(f'Extrato da conta {self.__numero_conta}')
        for transacao in self._transacoes:
            print(transacao)
            

    # def __str__(self):
    #     return f'Conta {self.numero}, Correntista: {self.nome_correntista}, Saldo: {self.saldo}'
    
# Test the class    
__name__ = '__main__'
conta_leonardo = ContaCorrente('Leonardo', '229.583.958-04', '1234', '030462')
conta_augusto = ContaCorrente('Augusto', '222.555.333-04', '9801', '076289')
conta_leonardo.depositar(3000)
print('.'*70)
conta_leonardo.resgatar(200)
print('.'*70)
conta_leonardo.consulta_extrato()
print('.'*70)
conta_leonardo.transferir(700, conta_augusto)
print('.'*70)




