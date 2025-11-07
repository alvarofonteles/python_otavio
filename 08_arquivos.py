'''
FASE 8 - Operações com Arquivos.
Como mover, copiar e apagar arquivos com Python - Aula 32.
'''

# %%
from pkgs.arcs.gerencia import gerir

try:
    caminho_arq_old = input('Digite seu caminho')
    caminho_arq_new = input('Digite seu caminho')
    acao_arq = input('Digite sua opção ("copy", "move", "delete")')

    ACAO = {'copy': 'COPIADOS', 'move': 'MOVIDOS', 'delete': 'DELETADOS'}

    gerencia = list(
        gerir(old_caminho=caminho_arq_old, new_caminho=caminho_arq_new, acao=acao_arq)
    )

    print(
        f'{len(gerencia)} arquivos, {ACAO[acao_arq]} para: "{caminho_arq_new}" com sucesso!\n'
    )

    for idx, arq in enumerate(gerencia, 1):
        print(f'Arquivo {idx}: "{arq}"')

except Exception as e:
    print(e)
