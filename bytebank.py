from conta import Conta
from cliente import Cliente
codigos = Conta.codigos_dos_bancos()
print(codigos)
print(codigos['BB'])
print(codigos['Caixa'])
print(codigos['Bradesco'])
