'''
FASE 6 - Pacotes e Módulos.
Como criar pacotes e módulos em Python - Aula 30.
'''


def real(valor: int | float) -> str:
    real = f'R${valor:.2f}'
    return real.replace('.', ',')  # R$0,00
