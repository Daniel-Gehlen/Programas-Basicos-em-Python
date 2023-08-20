def calcular_descont(valor, desconto=0):
    # Oparâmetro desconto possui valor zero default
    valor_com_desconto = valor -(valor * desconto)
    return valor_com_desconto

valor1 = Calcular_desconto(100) # Não aplicar nenhum desconto
valor2 = calcular_desconto(100, 0.25) # Aplicar desconto de 25%

print(f'\nPrimeiro valor a ser pago = {valor1}')
print(f'\nSegundo valor a ser pago = {valor2}')
