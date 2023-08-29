# Algoritmo de busca sequêncial ordenada while

def busca_sequncial(lista, elemento):
    pos = 0
    encontrado = False

    while pos < len(lista) and not encontrado:
        if lista[pos] == elemento:
            encontrado = True
        else:
            pos = pos+1

    return encontrado

testelista = [2, 10, 8, 15, 18, 20, 12, 1]

print(testelista)

pos = busca_sequncial(testelista, 15)

print(15, pos)

pos = busca_sequncial(testelista, 19)

print(19, pos)

# def busca_sequencial(lista, elemento):
#     pos = 0
#     encontrado = False
# Nesta linha, você está definindo uma função chamada busca_sequencial que aceita dois argumentos:
# lista (a lista na qual você deseja procurar) e elemento (o elemento que você está procurando na
# lista).
# pos é uma variável que será usada para acompanhar a posição atual durante a busca na lista.
# encontrado é uma variável booleana que será usada para determinar se o elemento foi encontrado
# na lista

#     while pos < len(lista) and not encontrado:
# Inicia um loop while. O loop continuará enquanto a posição atual (pos) for menor que
# o comprimento da lista e enquanto encontrado for False.

#         if lista[pos] == elemento:
        #     encontrado = True
        # else:
        #     pos = pos + 1
# Este bloco if verifica se o elemento na posição atual da lista (lista[pos]) é igual ao
# elemento que está sendo procurado (elemento).
# Se forem iguais, a variável encontrado é definida como True, indicando que o elemento foi 
# encontrado.
# Caso contrário, a posição pos é incrementada em 1 para continuar a busca na próxima posição 
# da lista.

#     return encontrado
# Após sair do loop, a função retorna o valor da variável encontrado, que indicará se o elemento
# foi encontrado (True) ou não (False)

# testelista = [2, 10, 8, 15, 18, 20, 12, 1]
# print(testelista)
# Aqui você cria uma lista chamada testelista e a imprime na saída.

# pos = busca_sequencial(testelista, 15)
# print(15, pos)
# Você chama a função busca_sequencial para procurar o elemento 15 na lista testelista.
# O resultado é armazenado na variável pos.
# Em seguida, você imprime o número 15 seguido do valor de pos.

# pos = busca_sequencial(testelista, 19)
# print(19, pos)
# Você chama novamente a função busca_sequencial, desta vez para procurar o elemento 19 na lista
# testelista.
# O resultado é armazenado em pos, e você imprime o número 19 seguido do valor de pos.

# Essencialmente, o código verifica se um determinado elemento está presente na lista usando 
# uma abordagem de busca sequencial, onde cada elemento da lista é verificado em ordem até que
# o elemento desejado seja encontrado ou até que a lista seja percorrida inteiramente.

