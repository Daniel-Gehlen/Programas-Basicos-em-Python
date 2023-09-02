def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

# Lista de números desordenados
numbers = [64, 34, 25, 12, 22]

# Chamando a função de ordenação quick sort
sorted_numbers = quick_sort(numbers)

# Imprimindo a lista ordenada
print("Lista ordenada:", sorted_numbers)


def quick_sort(arr):

#Explicação do Algoritmo

# def quick_sort(arr):
# Aqui, estamos definindo uma função chamada quick_sort que recebe uma lista arr como parâmetro.
# Essa função implementará o algoritmo de ordenação QuickSort.

# if len(arr) <= 1:
# Essa linha verifica se o comprimento da lista arr é 1 ou menor. Se for o caso, isso significa 
# que a lista já está ordenada (ou é vazia), e a função retorna a própria lista.

# return arr
# Se a lista arr tiver um comprimento igual a 1 ou estiver vazia, a função simplesmente retorna 
# a própria lista.

# pivot = arr[len(arr) // 2]
# Aqui, o pivô é selecionado a partir do elemento no meio da lista. O operador // realiza a 
# divisão inteira, obtendo o índice do elemento do meio.

# left = [x for x in arr if x < pivot]
# Esta linha cria uma nova lista chamada left, contendo todos os elementos da lista arr que 
# são menores do que o pivô.

# middle = [x for x in arr if x == pivot]
# Aqui, uma lista middle é criada, contendo todos os elementos da lista arr que são iguais 
# ao pivô.

# right = [x for x in arr if x > pivot]
# Essa linha cria uma lista right contendo todos os elementos da lista arr que são maiores que
# o pivô.

# return quick_sort(left) + middle + quick_sort(right)
# Nesta linha, a função quick_sort é chamada recursivamente para ordenar a lista left e 
# a lista right. Os resultados dessas chamadas recursivas são concatenados junto com 
# a lista middle, resultando na lista completamente ordenada.

# numbers = [64, 34, 25, 12, 22]
# Aqui, uma lista de números desordenados é criada para ser ordenada usando o algoritmo QuickSort.

# sorted_numbers = quick_sort(numbers)
# A função quick_sort é chamada com a lista de números desordenados como argumento, resultando
# na lista sorted_numbers, que conterá os números ordenados.

# print("Lista ordenada:", sorted_numbers)
# Finalmente, a lista ordenada é impressa na saída, mostrando os números em ordem crescente.
# No geral, o código implementa o algoritmo de ordenação QuickSort, que é baseado na estratégia 
# de dividir e conquistar, onde a lista é dividida em partições menores,
# ordenadas individualmente e depois combinadas para obter a lista totalmente ordenada.