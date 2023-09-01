number = 1
while number != 0:
    number = int(input('Digite um número: '))
    
    if number == 0:
        print('Programa encerrado.')
    elif number % 2 == 0:
        print('Número par')
    else:
        print('Número ímpar')
