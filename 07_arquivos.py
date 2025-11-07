'''
FASE 7 - Busca de Arquivos.
Como encontrar arquivos no sistema com Python - Aula 31.
'''

# %%
from pkgs.arcs.encontra import pesquisa

try:
    caminho_arq = input(
        'Digite seu caminho'
    )  # 'C:/Users/[Seu_Diretório]/OneDrive/Documentos'

    termo_arq = input('Digite seu arquivo de pesquisa')  #'CVs'

    arquivos = list(pesquisa(caminho=caminho_arq, termo=termo_arq))

    if arquivos:
        contador = 0
        for arquivo, caminho_arq, nome, extensao, tamanho, tam_formatado in arquivos:
            contador += 1
            print()
            print(f'Encontrei o arquivo: {arquivo}')
            print(f'Caminho: "{caminho_arq}"')
            print(f'Nome: {nome}')
            print(f'Extensão: {extensao}')
            print(f'Tamanho: {tamanho}')
            print(f'Tamanho Formatado: {tam_formatado}')

        print()
        print(f'Encontrado {contador} arquivos')
    else:
        print(f'Nenhum arquivo com "{termo_arq}" encontrado em "{caminho_arq}"')

except Exception as errm:
    print(errm)
