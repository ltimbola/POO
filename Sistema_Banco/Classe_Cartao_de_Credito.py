#%%
from datetime import datetime
import pytz
from random import randint

class Cartao_de_Credito:

    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('America/Sao_Paulo')
        hora_BR = datetime.now(fuso_BR)
        return hora_BR

    def __init__(self, titular, conta_corrente):
        self.limite = 1200
        self.numero_cartao = ' '.join([''.join([str(randint(0, 9)) for _ in range(4)]) for _ in range(4)])
        self.titular = titular
        self.validade = self._definiir_validade()
        self.cvv = ''.join([str(randint(0, 9)) for _ in range(3)])
        self._senha = None
        self.conta_corrente = conta_corrente
        self.fatura = []
        self.fatura_aberta = False
        conta_corrente.cartoes.append(self)

    def consultar_num_conta(self):
        print(f'O número da conta corrente é: {self.conta_corrente.consultar_numero_conta()}')
        return self.conta_corrente.consultar_numero_conta()

    def consultar_limite(self):
        print(f'O limite do cartão é de R$ {self.limite:,.2f}')
        return self.limite
    
    def alterar_limite(self, novo_limite):
        if self.conta_corrente._limite_da_conta() > novo_limite:
            self.limite = novo_limite
            print(f'O limite do cartão foi alterado para R$ {novo_limite:,.2f}')

        else:
            print(f'O limite do cartão não pode ser alterado para R$ {novo_limite:,.2f}')
        

    def _definiir_validade(self):
        if self.limite >= 1000:
            return f'{Cartao_de_Credito._data_hora().month}' + '/' + f'{Cartao_de_Credito._data_hora().year + 5}'

        else:
            return f'{Cartao_de_Credito._data_hora().month}' + '/' + f'{Cartao_de_Credito._data_hora().year + 2}'    

    def consultar_validade(self):
        print(f'A validade do cartão é: {self.validade}')
        return self.validade
    
    def consultar_numero_cartao(self):
        print(f'O número do cartão é: {self.numero_cartao}')
        return self.numero_cartao
    
    def consultar_cvv(self):
        print(f'O CVV do cartão é: {self.cvv}')
        return self.cvv
    
    @property
    def senha(self):
        return self._senha
    
    @senha.setter
    def senha(self, valor):
        if len(valor) == 4 and valor.isnumeric():
            self._senha = valor
        else:
            print('A senha deve ter 4 dígitos numéricos')



