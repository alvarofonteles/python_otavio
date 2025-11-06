'''
FASE 3 - Levantando Exceções.
Levantando exceções em Python (raise) - Aula 27.
'''


# %%
def divide(n1: int | float, n2: int | float) -> int | float:
    try:
        return n1 / n2
    except ZeroDivisionError as errm:
        print(f'Log Error: {errm}')  # Log Error: division by zero
        raise  # levantando exceção geral


ex1 = divide(n1=16.4, n2=4)
print(ex1)  # 4.1

# trantando local
try:
    ex2 = divide(1, 0)
    print(ex2)
except ZeroDivisionError as errm:
    print(f'ZeroDivisionError {errm}')  # ZeroDivisionError division by zero


# %%
def divide2(n1: int | float, n2: int | float) -> int | float:
    if n2 == 0:
        raise ValueError(
            f'(ValueError): n2: int | float, não pode ser 0'
        )  # levantando exceção personalizada
    return n1 / n2


# trantando local
try:
    ex3 = divide2(1, 0)
    print(ex3)
except ValueError as errm:
    print(f'Você, está tentando dividir por (0)')  #
    print(f'Log de Error {errm}')  # ValueError: n2: int | float, não pode ser 0

# %%
