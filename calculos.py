'''
FASE 5 - Criando Módulos.
Como criar módulos em Python - Aula 29.
'''

# %%
# Módulo calculos

from math import pi

# pi
PI = pi


# double
def dobra(lista):
    return [x * 2 for x in lista]


# mult
def multiplica(lista):
    ret = 1
    for x in lista:
        ret *= x
    return ret


# UM único if __name__,
def main():
    # pi
    print(f'PI: {PI}')  # PI: 3.141592653589793

    # double
    lista = [1, 2, 3, 4, 5]
    print(f'Dobra: {dobra(lista)}')  # Dobra: [2, 4, 6, 8, 10]

    # mult
    print(f'Multiplica: {multiplica(lista)}')  # Multiplica: 120

    # ... todos seus testes aqui


# pra rodar TUDO!
if __name__ == '__main__':
    main()
    # ... todos seus defs aqui
