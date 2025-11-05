'''
FASE 1 - Geradores, Iteradores e Iteráveis.
Geradores, Iteradores e Iteráveis em Python - Aula 25.
'''

# %%
import sys
import time


# %%
l1 = [1, 2, 3, 4, 5]

# É um Iterável __iter__?
print(hasattr(l1, '__iter__'))  # True

# É um Iterador __next__?
print(hasattr(l1, '__next__'))  # False

l1 = iter(l1)  # força ser um Iterador
print(hasattr(l1, '__next__'))  # True

# passa a iterar manualmente, pois virou Iterador
print(next(l1))  # 1
print(next(l1))  # 2
print(next(l1))  # 3

for x in l1:
    print(x)  # 1, 2, 3, 4, 5

# %%
l2 = list(range(1000))
print(sys.getsizeof(l2))  # 8056 bytes


# simulando um gerador
def gera():
    ret = []
    for x in range(5):
        ret.append(x)
        time.sleep(0.1)  # 1/2 seg
    return ret


ex1 = gera()
print(ex1)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for x in ex1:
    print(x)  # 0, 1, 2, 3, 4

# É um Iterador __next__?
print(hasattr(ex1, '__next__'))  # False


# gerado de fato
def gera2():
    for x in range(5):
        yield x
        time.sleep(0.1)  # 1/2 seg


ex2 = gera2()
print(ex2)  # <generator object gera2 at 0x0000017A0BC2C520>

# antes do for pra não dá exception
print(next(ex2))  # 0
print(next(ex2))  # 1
print(next(ex2))  # 2
print(next(ex2))  # 3
print(next(ex2))  # 4

for x in ex2:
    print(x)  # 0, 1, 2, 3, 4

# É um Iterável __iter__?
print(hasattr(ex2, '__iter__'))  # True

# É um Iterador __next__?
print(hasattr(ex2, '__next__'))  # True


# %%
# outra forma seria
def gera3():
    val = 'val1'
    yield val
    val = 'val2'
    yield val
    val = 'val3'
    yield val


ex3 = gera3()
print(ex3)  # <generator object gera3 at 0x0000018963E2A200>

print(next(ex3))  # val1
print(next(ex3))  # val2
print(next(ex3))  # val3

# também pode usar laço
for x in ex3:
    print(x)  # val1, val2, val3

# %%

l3 = list(range(10000))
print(type(l3))  # <class 'list'>
print(sys.getsizeof(l3))  # 80056

l4 = [x for x in range(10000)]
print(type(l4))  # <class 'list'>
print(sys.getsizeof(l4))  # 85176

# essa forma é mais pythonica de gerador
# sempre mantém, pois não itera tudo de uma vez
l5 = (x for x in range(10000))
print(type(l5))  # <class 'generator'>
print(sys.getsizeof(l5))  # 192
