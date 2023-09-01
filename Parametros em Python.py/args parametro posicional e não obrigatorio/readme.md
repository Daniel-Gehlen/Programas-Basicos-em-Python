def imprimir_parametros(*args):
    qtde_parametros = len(args)
    print(f'qtde_parametros = {qtde_parametros}')

    for i, valor in enumerate(args):
        print(f'Posição = {i}, valor = {valor}')

print('\nChamada 1')
imprimir_parametros('São Paulo', 10, 23, 78, 'João')
print('\nChamada 2')
imprimir_parametros(10, 'São Paulo')