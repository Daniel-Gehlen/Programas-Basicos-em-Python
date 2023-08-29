a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))

equacao = f'{a} * x + {b}'
print(f'\nA formula geral da equação linear é (a * x + b): {equacao}')

for x in range(5):
    y = eval(equacao)
    print(f'Resultado da equação para x = {x} é {y}')