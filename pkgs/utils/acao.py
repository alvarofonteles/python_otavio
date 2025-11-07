'''
FASE 8 - Operações com Arquivos.
Como mover, copiar e apagar arquivos com Python - Aula 32.
'''

from shutil import move, copy
from os import remove


def mover(old_caminho, new_caminho):
    try:
        move(old_caminho, new_caminho)
    except Exception as e:
        raise Exception(f'Erro ao mover "{old_caminho}" -> "{new_caminho}": {e}')


def copiar(old_caminho, new_caminho):
    try:
        copy(old_caminho, new_caminho)
    except Exception as e:
        raise Exception(f'Erro ao copiar "{old_caminho}" -> "{new_caminho}": {e}')


def deletar(caminho_arq):
    try:
        remove(caminho_arq)
    except Exception as e:
        raise Exception(f'Erro ao deletar "{caminho_arq}": {e}')
