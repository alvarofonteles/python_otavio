'''Material de Apoio.
O que é a '/' e o '*' nos parâmetros de funções do Python'''

# %%
# / (barra)
# Antes: só posicional
# depois: posicional ou nomeado

# * (asterisco)
# antes: posicional ou nomeado
# depois: só nomeado


# / → tudo à ESQUERDA = APENAS POSICIONAL (não pode usar nome)
# * → tudo à DIREITA = APENAS NOMEADO (deve usar nome=valor)


# 1. posicional
def name(nome, sobrenome, /, apelido):
    print(nome, sobrenome, apelido)


# válidos
name('Otávio', 'Miranda', 'Prof')

# inválidos - nome ou sobrenome não podem ser nomeados
# name(nome='Otávio', sobrenome='Miranda', 'Prof')
# name('Otávio', sobrenome='Miranda', 'Prof')


# 2. nomeado
def change_name(nome, sobrenome, *, remove):
    print(nome, sobrenome, remove)


# válidos
change_name('Otávio', 'Miranda', remove=True)
change_name(nome='Otávio', sobrenome='Miranda', remove=False)
change_name('Otávio', sobrenome='Miranda', remove=True)

# inválidos - remove deve ser nomeados
# change_name('Otávio', 'Miranda', True)


# 3. pósicional e nomeado
def name2(nome, /, *, sobrenome, apelido):
    print(nome, sobrenome, apelido)


# válidos
name2('Otávio', sobrenome='Miranda', apelido='Prof')


# inválidos
# name('Otávio', sobrenome='Miranda', 'Prof')
# name('Otávio', 'Miranda', apelido='Prof')
# name(nome='Otávio', sobrenome='Miranda', apelido='Prof')


# 4. pósicional e nomeado
def change_name2(nome, /, sobrenome, *, remove):
    print(nome, sobrenome, remove)


# válidos
change_name2('Otávio', sobrenome='Miranda', remove=False)
change_name2('Otávio', 'Miranda', remove=False)

# inválidos
# change_name(nome='Otávio', sobrenome='Miranda', False)
# change_name(nome='Otávio', 'Miranda', remove=False)


# Válidos - todas as combinações possíveis
def name3(nome, sobrenome, apelido, /):
    print(nome, sobrenome, apelido)


def change_name3(*, nome, sobrenome, remove):
    print(nome, sobrenome, remove)


# Sintaxe inválida - não pode ter / e * consecutivos
# def name4(nome, sobrenome, apelido, /, *):
#     print(nome, sobrenome, apelido)

# def change_name4(/,*, nome, sobrenome, remove):
#     print(nome, sobrenome, remove)


# %%
# Extra Avançado (*args & **kwargs)


# 5. *args para número variável de argumentos POSICIONAIS
def soma_args(*args):
    '''*args coleta argumentos POSICIONAIS extras em uma tupla'''
    return sum(args)


print(soma_args(1, 2, 3, 4, 5))  # 15
print(soma_args(10, 20))  # 30


# %%
# 6. **kwargs para número variável de argumentos NOMEADOS
def print_kwargs(**kwargs):
    '''**kwargs coleta argumentos NOMEADOS extras em um dicionário'''
    for chave, valor in kwargs.items():
        print(f'{chave}: {valor}')


print_kwargs(
    nome='Otávio', idade=40, cidade='RJ'
)  # nome: Otávio, idade: 400, cidade: RJ


# %%
# 7. Combinação completa
def funcao_completa(a, b, /, c, d, *args, e, f, **kwargs):
    '''
    a, b: apenas posição
    c, d: posição ou nome
    args: argumentos posicionais extras
    e, f: apenas nome
    kwargs: argumentos nomeados extras
    '''
    print(f'a={a}, b={b}, c={c}, d={d}')  # a=1, b=2, c=3, d=4
    print(f'args={args}, e={e}, f={f}')  # args=(5, 6), e=7, f=8
    print(f'kwargs={kwargs}')  # kwargs={'x': 9, 'y': 10}


funcao_completa(1, 2, 3, 4, 5, 6, e=7, f=8, x=9, y=10)
