def calcular_desconto(valor, desconto):
    # O parâmetro desconto não possui valor default
    valor_com_desconto = valor - (valor * desconto)
    return valor_com_desconto

valor1 = calcular_desconto(100, 0)  # Não aplicar nenhum desconto
valor2 = calcular_desconto(100, 0.25)  # Aplicar desconto de 25%

print(f'\nPrimeiro valor a ser pago = {valor1}')
print(f'Segundo valor a ser pago = {valor2}')

