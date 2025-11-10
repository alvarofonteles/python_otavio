'''
FASE 9 - Leitura e Escrita de Arquivos.
Como criar, ler e escrever arquivos com Python - Aula 33
'''

# %%
from pkgs.arcs.edita import editar

# View
try:
    ACAO = {'create': 'CRIADO', 'read': 'LIDO', 'write': 'ESCRITO'}

    # inputs
    caminho = input('Digite caminho (ex: arquivo.txt ou dados.json): ')
    acao_arq = input('Ação (create/read/write): ')

    # detecta extensão
    if caminho.lower().endswith('.json'):
        tipo = 'JSON'
        if acao_arq in ('create', 'write'):
            # Input JSON
            profissao = input('Profissão: ')
            nome = input('Nome: ')
            techs = input('Techs (separadas por vírgula): ').split(',')
            conteudo = {profissao: [{'nome': nome, 'tech': [t.strip() for t in techs]}]}
        else:
            conteudo = ''  # read sem conteúdo
    else:
        tipo = 'TXT'
        if acao_arq in ('create', 'write'):
            conteudo = input('Digite o texto: ')
        else:
            conteudo = ''

    print(f'=== Processando arquivo {tipo} ===')

    edita = list(editar(caminho=caminho, txt=conteudo, acao=acao_arq))

    print(f'{len(edita)} arquivo {tipo} {ACAO[acao_arq]} com sucesso!')

    for conteudo, caminho in edita:
        print(f'Conteúdo {tipo}: {conteudo}')
        print(f'Caminho: {caminho}')

        # formata conteúdo baseado no tipo
        if tipo == 'JSON' and acao_arq == 'read':
            for profissao, pessoas in conteudo.items():  # loop por profissão
                print(f'Profissão: {profissao}')
                for pessoa in pessoas:
                    print(f'  Nome: {pessoa["nome"]}')
                    print(f'  Techs: {", ".join(pessoa["tech"])}')
        elif tipo == 'TXT' and acao_arq == 'read':
            print(f'Linhas: {len(conteudo.splitlines())}')

except Exception as e:
    print(e)
