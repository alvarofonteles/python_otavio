'''Material de Apoio.
Map, filter e reduce em Python.'''

# %%

produtos = [
    {'nome': 'P1', 'preco': 59.90, 'peso_kg': 1.312, 'variacoes': ['a', 'b']},
    {'nome': 'P2', 'preco': 19.55, 'peso_kg': 2.300, 'variacoes': ['c', 'd']},
    {'nome': 'P3', 'preco': 9.13, 'peso_kg': 0.150, 'variacoes': ['e', 'f']},
    {'nome': 'P4', 'preco': 3.49, 'peso_kg': 0.789, 'variacoes': ['g', 'h']},
]

# 1 - filter basico - objeto iterador
preco = filter(lambda p: p['preco'] > 10, produtos)
print(preco)  # objeto filter

# 2 - filter convertido para lista
preco = list(filter(lambda p: p['preco'] > 10, produtos))
print(
    preco
)  # [{'nome': 'P1', 'peso_kg': 1.312, 'preco': 59.9, 'variacoes': ['a', 'b']}, {'nome': 'P2', 'peso_kg': 2.3, 'preco': 19.55, 'variacoes': ['c', 'd']}]

# 3 - pipeline filter -> map -> list - apenas preços
preco = list(map(lambda p: p['preco'], filter(lambda p: p['preco'] > 10, produtos)))
print(f'preço filtrado: {preco}')  # [59.9, 19.55]

# 4 - list comprehension - produtos completos
preco = [p for p in produtos if p['preco'] > 10]
print(
    preco
)  # [{'nome': 'P1', 'preco': 59.9, 'peso_kg': 1.312, 'variacoes': ['a', 'b']}, {'nome': 'P2', 'preco': 19.55, 'peso_kg': 2.3, 'variacoes': ['c', 'd']}]

# 5 - list comprehension - apenas preços
preco = [p['preco'] for p in produtos if p['preco'] > 10]
print(f'preço filtrado comp: {preco}')  # [59.9, 19.55]
