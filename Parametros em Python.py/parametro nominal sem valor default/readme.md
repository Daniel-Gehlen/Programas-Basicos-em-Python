def converter_maiuscula(texto, flag_maiuscula):
    if flag_maiuscula:
        return texto.upper()
    else:
        return texto.lower()

texto = converter_maiuscula(texto='João', flag_maiuscula=True)  # Passagem nominal de parâmetro
print(texto)
