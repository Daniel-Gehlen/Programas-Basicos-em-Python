def busca_linear(lista, valor):
    for i in range(len(lista)):
        if lista[i] == valor:
            return i  # Retorna o índice onde o valor foi encontrado
    return -1  # Retorna -1 se o valor não foi encontrado na lista

# Exemplo de uso
numeros = [12, 45, 67, 23, 9, 34, 78, 56]
valor_procurado = 34

indice = busca_linear(numeros, valor_procurado)

if indice != -1:
    print(f"O valor {valor_procurado} foi encontrado no índice {indice}.")
else:
    print(f"O valor {valor_procurado} não foi encontrado na lista.")

# Neste exemplo, a função busca_linear percorre a lista de números item por item, 
# comparando cada elemento com o valor procurado. Se o elemento for igual ao valor procurado,
# a função retorna o índice onde o valor foi encontrado. Se nenhum elemento correspondente for 
# encontrado, a função retorna -1.

# A complexidade no pior caso para esse algoritmo é O(n), 
# onde n é o número de elementos na lista. Isso ocorre porque, 
# no pior caso, você precisaria percorrer todos os elementos da lista para determinar 
# se o valor procurado está presente ou não.

# Esse algoritmo é simples e funciona bem para conjuntos de dados pequenos e não ordenados.
#  No entanto, para conjuntos de dados maiores ou ordenados, algoritmos de busca mais eficientes,
#  como a busca binária, são geralmente preferidos devido à sua menor complexidade