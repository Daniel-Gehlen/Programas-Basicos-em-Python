a = 2
b= 1

equação = input('Digite a formula geral da equação linear (a * x + b): ')
print(f'\nA entrada do usuário {equação} é do tipo {type(equação)}')

for x in range(5):
    y = eval(equação)
    print(f'\nResultado da equação para x = {x} e {y}')