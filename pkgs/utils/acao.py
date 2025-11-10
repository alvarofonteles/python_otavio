'''
FASE 8 - Operações com Arquivos.
Como mover, copiar e apagar arquivos com Python - Aula 32.
'''

from shutil import move, copy
from os import remove, path
from json import dump, load


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


# Model
def criar(caminho, txt):
    try:
        with open(caminho, 'w', encoding='utf-8') as file:
            if caminho.endswith('.json'):
                # dict para JSON
                if isinstance(txt, dict):
                    dump(txt, file, indent=2, ensure_ascii=False)
                else:
                    file.write(txt)
            else:
                file.write(txt)
    except Exception as e:
        raise Exception(f'Erro ao criar "{caminho}": {e}')


def ler(caminho):
    try:
        with open(caminho, 'r', encoding='utf-8') as file:
            if caminho.endswith('.json'):
                return load(file)  # retorna dict
            else:
                return file.read()  # string
    except Exception as e:
        raise Exception(f'Erro ao ler "{caminho}": {e}')


# Avanaçado by ajuda DeepSeek
def escrever(caminho, txt):
    try:
        if caminho.endswith('.json'):
            if path.exists(caminho):
                with open(caminho, 'r', encoding='utf-8') as file:
                    dados = load(file)
            else:
                dados = {}  # dict vazio

            # merge por profissão + nome
            for profissao, pessoas in txt.items():
                # garante profissão existe (equivale ao if not in)
                dados.setdefault(profissao, [])

                nova_pessoa = pessoas[0]

                # busca pessoa com next() + generator
                pessoa_existente = next(
                    (p for p in dados[profissao] if p['nome'] == nova_pessoa['nome']),
                    None,  # retorna None se não encontrar
                )

                if pessoa_existente:
                    # extend() + generator para adicionar techs novas
                    pessoa_existente['tech'].extend(
                        tech
                        for tech in nova_pessoa['tech']
                        if tech
                        not in pessoa_existente['tech']  # só adiciona se não existe
                    )
                else:
                    dados[profissao].append(nova_pessoa)

            with open(caminho, 'w', encoding='utf-8') as file:
                dump(dados, file, indent=2, ensure_ascii=False)
        else:
            with open(caminho, 'a', encoding='utf-8') as file:
                file.write(txt + '\n')
    except Exception as e:
        raise Exception(f'Erro ao escrever "{caminho}": {e}')
