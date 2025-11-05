'''
FASE 2 - Tratamento de Exceções.
Try, Except - Tratando Exceções em Python - Aula 26
'''

# %%

# Error 1
try:
    a: None
    print(a)
except NameError as e:
    print(f'NameError: {e}')  # NameError: name 'a' is not defined

# Error 2
try:
    b = []
    print(b[1])
except IndexError as e:
    print(f'IndexError: {e}')  # IndexError: list index out of range

# Error 3
try:
    c = {}
    print(c[1])
except KeyError as e:
    print(f'KeyError: {e}')  # KeyError: 1

# Sem Error
try:
    val = (1, 2)
    print(val)  # (1, 2)
except NameError as errm:
    print(f'error {errm}')
except IndexError as e:
    print(f'IndexError: {e}')
except (Exception, KeyError) as e:
    print(f'KeyError: {e}')
else:
    print('Seu code, rodeu, mas com Erro!')  # Seu code, rodeu, mas com Erro!
finally:
    print('Finalmente!!!')  # Finalmente!!!

print('continua...')  # continua...

# Error 5 Tratado no Finally
try:
    val2 = 1 / 0
    print(val2)
except Exception as e:
    print(f'Exception: {e}')  # Exception: division by zero
finally:
    val2 = None

print(val2)  # None

# Error 6 Try dentro de outro Try
try:
    val3 = 0
    try:
        val3 = 1 / 0
        print(val3)
    except Exception as e:
        print(f'Exception 1: {e}')  # Exception 1: division by zero
except Exception as e:
    print(f'Exception 2: {e}')
