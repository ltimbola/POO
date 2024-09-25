#%%
from Classe_Conta_Corrente import ContaCorrente
from Classe_Cartao_de_Credito import Cartao_de_Credito

# Create the accounts
conta_leonardo = ContaCorrente('Leonardo', '229.583.958-04', '1234', '030462')
conta_augusto = ContaCorrente('Augusto', '222.555.333-04', '9801', '076289')

# Create the credit cards
Cartao_leo = Cartao_de_Credito('Leonardo', conta_leonardo)
Cartao_timbola = Cartao_de_Credito('Timbola', conta_leonardo)
cartao_augusto = Cartao_de_Credito('Augusto', conta_augusto)
print('-'*50)

# Doing deposits, withdrawals and transfers
# Deposits
conta_leonardo.depositar(5000)
conta_augusto.depositar(5000)
print('-'*50)

# Withdrawals
conta_leonardo.resgatar(200)
conta_augusto.resgatar(200)
print('-'*50)

# Transfers
conta_leonardo.transferir(300, conta_augusto)
print('-'*50)

# Info about the Credit Cards
# Cartao_leo.consultar_num_conta()
# Cartao_leo.consultar_validade()
# Cartao_leo.consultar_numero_cartao()
# Cartao_leo.consultar_cvv()
# Cartao_leo.alterar_limite(3000)
print('-'*50)

# Discovering the credit cards of the account
conta_leonardo.cartoes_da_conta()
