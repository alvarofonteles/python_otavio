'''
FASE 6 - Pacotes e Módulos.
Como criar pacotes e módulos em Python - Aula 30.
'''

# %%


from pkg_vendas.calc_preco import aumento, reducao
from pkg_vendas.formata.preco import real

print(aumento(250, 15))  # 287.5
print(aumento(100, 10, True))  # R$110,00
print(reducao(1000, 10, False))  # 900.0

print(real(50))  # R$50,00
