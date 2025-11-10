'''
FASE 9 - Leitura e Escrita de Arquivos.
Como criar, ler e escrever arquivos com Python - Aula 33
'''

# %%
import os
from typing import Literal
from ..utils.acao import criar, ler, escrever


# Controller
def editar(caminho: str, txt: str, acao: Literal['create', 'read', 'write']):

    if '/' in caminho or '\\' in caminho:
        caminho_final = caminho  # Usa o caminho do usuário
    else:
        caminho_final = f'pkgs/docs/{caminho}'  # Padrão docs/

    if acao in ['create', 'write']:
        os.makedirs(os.path.dirname(caminho_final), exist_ok=True)

    if acao == 'create':
        criar(caminho_final, txt)
        yield txt, caminho_final
    elif acao == 'read':
        conteudo = ler(caminho_final)  # Pega o conteúdo lido
        yield conteudo, caminho_final  # Yield o conteúdo
    elif acao == 'write':
        escrever(caminho_final, txt)
        yield txt, caminho_final
