'''
FASE 4 - Módulos Padrão.
Módulos padrão do Python - Aula 28.
'''

# %%
import sys

# sys.copyright
# sys.getsizeof
# sys.path

print(sys.platform)  # win32

# %%
import random

for x in range(5):
    print(random.randint(0, 10))  # 6, 10, 6, 9, 4

for x in range(5):
    print(
        random.random()
    )  # 0.3211495819906032, 0.17571639957044405, 0.49144090350965564, 0.663295...

# %%
from random import randint


def randint():
    return 'kkk'


ex1 = randint()  # sobreescreve
print(ex1)  # kkk

for x in range(3):
    print(ex1)  # kkk, kkk, kkk


# %%
from random import randint as ri


def randint(*args):
    return 'kkk'


ex1 = randint()  # sobreescreve
print(ex1)  # kkk

ex2 = ri(0, 5)  # usando o módulo
print(ex2)  # 4

for x in range(3):
    print(f'{ex1} e {ri(0, 5)}')  # kkk e 3, kkk e 0, kkk e 2

# %%
import os
import re

...  # Ellipsis
