'''Material de Apoio.
Map, filter e reduce em Python.'''

# %%
from pprint import pprint

_print = print  # backup
print = pprint  # temporário
# print = _print  # restaura

produtos = [
    {'nome': 'P1', 'preco': 59.90, 'peso_kg': 1.312, 'variacoes': ['a', 'b']},
    {'nome': 'P2', 'preco': 19.55, 'peso_kg': 2.300, 'variacoes': ['c', 'd']},
    {'nome': 'P3', 'preco': 9.13, 'peso_kg': 0.150, 'variacoes': ['e', 'f']},
    {'nome': 'P4', 'preco': 3.49, 'peso_kg': 0.789, 'variacoes': ['g', 'h']},
]

# print(produtos)

print('1. map sem list')
precos = map(lambda p: p['preco'], produtos)  # Iterator
print('next()')
print(next(precos))  # 59.9
print(next(precos))  # 19.55

print('inicio for')
for preco in precos:
    print(preco)  # 9.13, 3.49
print('fim')
print('')

print('2. for tradicional')
precos = []
for produto in produtos:
    precos.append(produto['preco'])  # [59.9, 19.55, 9.13, 3.49]

print(precos)
print('')

print('3. Map com list')
precos = list(map(lambda p: p['preco'], produtos))
print(precos)  # [59.9, 19.55, 9.13, 3.49]
print('')

# %%

produtos = [
    {'nome': 'P1', 'preco': 59.90, 'peso_kg': 1.312, 'variacoes': ['a', 'b']},
    {'nome': 'P2', 'preco': 19.55, 'peso_kg': 2.300, 'variacoes': ['c', 'd']},
    {'nome': 'P3', 'preco': 9.13, 'peso_kg': 0.150, 'variacoes': ['e', 'f']},
    {'nome': 'P4', 'preco': 3.49, 'peso_kg': 0.789, 'variacoes': ['g', 'h']},
]

print('3.1 Map com list')
print('')

print('Com ajuste de 5%')
precos = list(map(lambda p: round(p['preco'] * 1.05), produtos))
print(precos)  # [63, 21, 10, 4]
print('')

print('Remontando Com ajuste de 5%')
precos = list(map(lambda p: {'preco': round(p['preco'] * 1.05)}, produtos))
print(precos)  # [{'preco': 63}, {'preco': 21}, {'preco': 10}, {'preco': 4}]
print('')

print(f'Produtos antes!')
print(
    produtos
)  # [{'nome': 'P1', 'preco': 59.9, 'peso_kg': 1.312, 'variacoes': ['a', 'b']}, {'nome': 'P2', 'preco': 19.55, 'peso_kg': 2.3, 'variacoes': ['c', 'd']}, {'nome': 'P3', 'preco': 9.13, 'peso_kg': 0.15, 'variacoes': ['e', 'f']}, {'nome': 'P4', 'preco': 3.49, 'peso_kg': 0.789, 'variacoes': ['g', 'h']}]
print('')

print('Remontando e Sobrescrevendo (unpack) Com ajuste de 5%')
precos = list(map(lambda p: {**p, 'preco': round(p['preco'] * 1.05)}, produtos))

print(f'Produtos depois!')
print(
    precos
)  # [{'nome': 'P1', 'preco': 63, 'peso_kg': 1.312, 'variacoes': ['a', 'b']}, {'nome': 'P2', 'preco': 21, 'peso_kg': 2.3, 'variacoes': ['c', 'd']}, {'nome': 'P3', 'preco': 10, 'peso_kg': 0.15, 'variacoes': ['e', 'f']}, {'nome': 'P4', 'preco': 4, 'peso_kg': 0.789, 'variacoes': ['g', 'h']}]
print('')

print('4. List Comprehension')
precos = [p['preco'] for p in produtos]
print(precos)  # [59.9, 19.55, 9.13, 3.49]
print('')

# %%
# Extra Avançado com Geradores (# Ambos são LAZY)

produtos = [
    {'nome': 'P1', 'preco': 59.90, 'peso_kg': 1.312, 'variacoes': ['a', 'b']},
    {'nome': 'P2', 'preco': 19.55, 'peso_kg': 2.300, 'variacoes': ['c', 'd']},
    {'nome': 'P3', 'preco': 9.13, 'peso_kg': 0.150, 'variacoes': ['e', 'f']},
    {'nome': 'P4', 'preco': 3.49, 'peso_kg': 0.789, 'variacoes': ['g', 'h']},
]

print('Generator - Basico')
precos = (p['preco'] for p in produtos)  # yield
print(precos)  # generador do objeto (generator object)
print('')

print('1. Convertendo pra lista (mais facil)')
precos = (p['preco'] for p in produtos)
print(list(precos))  # [59.9, 19.55, 9.13, 3.49]
print('')

print('2. Loop direto (memory efficient)')
precos = (p['preco'] for p in produtos)
for preco in precos:
    print(preco)  # 59.9, 19.55, 9.13, 3.49
print('')

print('3. Next() manual (controle fino)')
precos = (p['preco'] for p in produtos)
print(next(precos))  # 59.9
print(next(precos))  # 19.55
print('')

print('4. Em pipelines (top)')
precos_altos = (p for p in produtos if p['preco'] > 9)  # com filtro
nomes = (p['nome'] for p in precos_altos)
print(list(nomes))  # ['P1', 'P2', 'P3']
print('')

print('5. Funcoes built-in (eficiente)')
precos = (p['preco'] for p in produtos)
soma = sum(precos)  # Soma sem criar lista
print(f'Soma: {soma}')  # Soma: 92.07
print('')

# Observação
# Ambos são LAZY
precos_gera = (p['preco'] for p in produtos)  # Expressão Generadora
precos_map = map(lambda p: p['preco'], produtos)  # Objeto Map

print(f'Geradoror: {next(precos_gera)}')  # Geradoror: 59.9
print(f'Map: {next(precos_map)}')  # Map: 59.9
