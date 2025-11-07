'''
FASE 8 - Operações com Arquivos.
Como mover, copiar e apagar arquivos com Python - Aula 32.
'''

import os
from typing import Generator, Literal, Tuple
from ..utils.acao import mover, copiar, deletar


# Usando Gerador
def gerir(
    old_caminho: str, new_caminho: str, acao: Literal['copy', 'move', 'delete']
) -> Generator[Tuple[str], None, None]:

    # Verifica o caminho base
    if not os.path.exists(old_caminho):
        raise FileNotFoundError(f'Caminho não existe: "{old_caminho}"')

    if not os.path.exists(new_caminho):
        # raise FileNotFoundError(f'Caminho não existe: "{caminho_new}"')
        os.mkdir(new_caminho)

    # Loop, pra cada arquivo:
    for raiz, diretorios, arquivos in os.walk(old_caminho):
        for arquivo in arquivos:
            old_caminho_completo = os.path.join(raiz, arquivo).replace(
                os.sep, '/'
            )  # altera a barra \

            new_caminho_completo = os.path.join(new_caminho, arquivo).replace(
                os.sep, '/'
            )  # altera a barra \

            if acao == 'copy':
                copiar(old_caminho_completo, new_caminho_completo)
                yield old_caminho_completo
            elif acao == 'move':
                mover(old_caminho_completo, new_caminho_completo)
                yield old_caminho_completo
            else:
                deletar(new_caminho_completo)  # escolha o local
                yield old_caminho_completo
