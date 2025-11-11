'''material de apoio.
map, filter e reduce em python.'''

# %%
from functools import reduce

produtos = [
    {'nome': 'P1', 'preco': 59.90, 'peso_kg': 1.312, 'variacoes': ['a', 'b']},
    {'nome': 'P2', 'preco': 19.55, 'peso_kg': 2.300, 'variacoes': ['c', 'd']},
    {'nome': 'P3', 'preco': 9.13, 'peso_kg': 0.150, 'variacoes': ['e', 'f']},
    {'nome': 'P4', 'preco': 3.49, 'peso_kg': 0.789, 'variacoes': ['g', 'h']},
]


# 1 - reduce com função definida (soma de preços)
def soma(soma, p):
    return soma + p['preco']


preco_total = reduce(soma, produtos, 0)
print(f'total com def: {preco_total}')  # total: 92.07

# 2 - reduce com lambda (soma de preços)
preco_total = reduce(lambda ac, p: ac + p['preco'], produtos, 0)
print(f'total com lambda: {preco_total}')  # total com lambda: 92.07

# 3 - alternativa com sum + list comprehension
preco_total = sum([p['preco'] for p in produtos])
print(preco_total)  # 92.07

# 4 - reduce para encontrar produto mais caro (acumulador = dicionário)
produto_mais_caro = reduce(
    lambda ac, p: p if p['preco'] > ac['preco'] else ac,
    produtos,
    produtos[0],  # valor inicial = primeiro produto
)
print(
    f'maior preço: {produto_mais_caro["nome"]} valor: {produto_mais_caro["preco"]}'
)  # P1

# 5 - reduce para concatenar variações (acumulador = lista)
todas_variacoes = reduce(lambda ac, p: ac + p['variacoes'], produtos, [])
print(f'variações: {todas_variacoes}')  # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

# 6 - reduce para concatenar nomes (acumulador = string)
nomes_concatenados = reduce(lambda ac, p: ac + p['nome'] + ', ', produtos, '')
print(f'nomes: {nomes_concatenados}')  # P1, P2, P3, P4,
