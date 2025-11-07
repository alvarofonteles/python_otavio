'''
FASE 7 - Busca de Arquivos.
Como encontrar arquivos no sistema com Python - Aula 31.
'''

import os
from typing import Generator, Tuple
from ..utils.formata import tamanho


# Usando Gerador
def pesquisa(caminho: str, termo: str) -> Generator[
    Tuple[str, str, str, str, int],  # O que YIELD retorna (sua tupla)
    None,  # O que SEND envia (não usa)
    None,  # O que RETURN final (não usa, tem o YIELD)
]:
    # Verifica o caminho base
    if not os.path.exists(caminho):
        raise FileNotFoundError(f'Caminho não existe: "{caminho}"')

    # Loop, pra cada arquivo:
    for raiz, diretorios, arquivos in os.walk(caminho):
        for arquivo in arquivos:
            if termo in arquivo:
                caminho_completo = os.path.join(raiz, arquivo).replace(
                    os.sep, '/'
                )  # altera a barra \

                # Verifica o arquivo específico
                if not os.path.exists(caminho_completo):
                    raise FileNotFoundError(f'Arquivo sumiu: {caminho_completo}')

                if not os.access(caminho_completo, os.R_OK):  # dica do chatboot
                    raise PermissionError(f'Sem permissão: {caminho_completo}')

                # Processa
                nome_arquivo, ext_arquivo = os.path.splitext(arquivo)
                tamanho_aquivo = os.path.getsize(caminho_completo)  # bytes
                tamanho_formatado = tamanho(tamanho_aquivo).replace('.', ',')

                # Gerador é melhor para MUITOS arquivos
                yield (
                    arquivo,
                    caminho_completo,
                    nome_arquivo,
                    ext_arquivo,
                    tamanho_aquivo,
                    tamanho_formatado,
                )
                # ↑ Baixo uso de memória, processamento lazy


# Exemplo Extra Base
# LISTA, é melhor para POUCOS arquivos
def pesquisa_lista_tupla(caminho: str, termo: str) -> list:
    caminho_procura = caminho  #'C:/Users/[Seu_Diretorio]/OneDrive/Documentos'
    termo_procura = termo  #'CV'
    resultados = []

    for raiz, diretorios, arquivos in os.walk(caminho_procura):
        for arquivo in arquivos:
            if termo_procura in arquivo:
                caminho_completo = os.path.join(raiz, arquivo)
                nome_arquivo, ext_arquivo = os.path.splitext(arquivo)
                tamanho_aquivo = os.path.getsize(caminho_completo)  # bytes

                resultados.append(
                    (
                        arquivo,
                        caminho_completo,
                        nome_arquivo,
                        ext_arquivo,
                        tamanho_aquivo,
                    )
                )
                # ↑ Mais simples, mas consome mais RAM

    return resultados
