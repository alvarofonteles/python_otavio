'''
FASE 7 - Busca de Arquivos.
Como encontrar arquivos no sistema com Python - Aula 31.
'''


def tamanho(tam: int) -> str:

    base = 1024
    kilo = base
    mega = base**2
    giga = base**3
    tera = base**4
    peta = base**5

    if tam < kilo:
        ret = 'B'
    elif tam < mega:
        tam /= kilo
        ret = 'K'
    elif tam < giga:
        tam /= mega
        ret = 'M'
    elif tam < tera:
        tam /= giga
        ret = 'G'
    elif tam < peta:
        tam /= tera
        ret = 'T'
    else:
        tam /= peta
        ret = 'P'
    tam = round(tam, 2)
    return f'{tam}{ret}'
