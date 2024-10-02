#%%

class Agencia:
    
    def __init__(self, nome, id_agencia, telefone, email, endereco):
        self.nome = nome
        self.id_agencia = id_agencia
        self.telefone = telefone
        self.email = email
        self.endereco = endereco
        self.contas_correntes = []
        self.cartoes_de_credito = []
        self.clientes = []
        self.emprestimos = []
        self.caixa = 0
        
    def verificar_caixa(self):
        if self.caixa < -1_000_000:
            print(f'O caixa da agência {self.id_agencia} está negativo em R$ {self.caixa:,.2f}, abaixo do nivel mínimo de R$ 1.000.000,00')
            return self.caixa
        else:    
            print(f'O caixa da agência {self.id_agencia} é de R$ {self.caixa:,.2f}, nivel adequado.')
            return self.caixa
        
    def emprestimo(self, valor, cpf, juros):
        
        if self.caixa >= valor:
            self.caixa -= valor
            self.emprestimos.append((cpf, valor, juros))
            print(f'Empréstimo de R$ {valor:,.2f} efetuado com sucesso')
            self.verificar_caixa()

    def listar_contas_correntes(self):
        print('Contas correntes da agência:')
        for conta in self.contas_correntes:
            print(conta.consultar_numero_conta())


class Agencia_Premium_plus(Agencia):

    def __init__(self, nome, telefone, email, endereco):
        super().__init__(nome,'0001', telefone, email, endereco)
        self.contas_correntes = []
        self.cartoes_de_credito = []
        self.clientes = []
        self.emprestimos = []
        self.caixa = 1_000_000
        
    def verificar_caixa(self):
        if self.caixa < -1_000_000:
            print(f'O caixa da agência {self.id_agencia} está negativo em R$ {self.caixa:,.2f}, abaixo do nivel mínimo de R$ 1.000.000,00')
            return self.caixa
        else:    
            print(f'O caixa da agência {self.id_agencia} é de R$ {self.caixa:,.2f}, nivel adequado.')
            return self.caixa
        
    def emprestimo(self, valor, cpf, juros):
        
        if self.caixa >= valor:
            self.caixa -= valor
            self.emprestimos.append((cpf, valor, juros))
            print(f'Empréstimo de R$ {valor:,.2f} efetuado com sucesso')
            self.verificar_caixa()

    def listar_contas_correntes(self):
        print('Contas correntes da agência:')
        for conta in self.contas_correntes:
            print(conta.consultar_numero_conta())    
    

__name__ == '__main__'        
agencia_1 = Agencia('Agência 1', '001', '11 99999-9999', 'agencia_1@gmail.com', 'Avenida Faria Lima, 1000')
agencia_1.verificar_caixa()