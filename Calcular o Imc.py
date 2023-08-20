# Então, a fórmula fica assim: IMC = Peso / Altura².

peso = float(input('Informe seu peso: '))
altura = float(input('Informe a sua altura: '))
imc = peso / (pow(altura, 2))

print(f'Seu imc é {imc:.2f}')

if imc < 18.5:
    print('Abaixo do peso')
elif 18.5 <= imc < 24.9:
    print('Peso normal')
elif 25 <= imc < 29.9:
    print('Acima do peso')
elif 30 <= imc < 34.9:
    print('Obesidade I')
elif 35 <= imc < 39.9:
    print('Obesidade II')
else:
    print('Obesidade III')