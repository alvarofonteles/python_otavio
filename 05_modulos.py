'''
FASE 5 - Criando Módulos.
Como criar módulos em Python - Aula 29.
'''

# %%
from calculos import dobra, multiplica, PI

print(f'PI: {PI}')  #  PI: 3.141592653589793

lista = [5, 4, 3, 2, 1]
print(f'Dobra: {dobra(lista)}')  # Dobra: [10, 8, 6, 4, 2]
print(f'Multiplica: {multiplica(lista)}')  # Multiplica: 120
