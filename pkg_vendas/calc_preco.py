'''
FASE 6 - Pacotes e Módulos.
Como criar pacotes e módulos em Python - Aula 30.
'''

from .formata.preco import real


def aumento(valor: int | float, perc: int | float, format: bool = False) -> str:
    valor += valor * (perc / 100)

    # verboso
    if format:
        return real(valor)
    else:
        return valor


def reducao(valor: int | float, perc: int | float, format: bool = False) -> str:
    valor -= valor * (perc / 100)
    return real(valor) if format else valor  # pythonico
