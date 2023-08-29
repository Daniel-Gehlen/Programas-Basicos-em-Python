def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2
    left_half = arr[:middle]
    right_half = arr[middle:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)

def merge(left, right):
    result = []
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result.extend(left[left_index:])
    result.extend(right[right_index:])
    return result

# Lista de números desordenados
numbers = [64, 34, 25, 12, 22]

# Chamando a função de ordenação merge sort
sorted_numbers = merge_sort(numbers)

# Imprimindo a lista ordenada
print("Lista ordenada:", sorted_numbers)

# Explicação do Algoritmo

# def merge_sort(arr):
# Definição da função merge_sort que recebe uma lista como entrada e irá ordená-la.

#     if len(arr) <= 1:
#        return arr
# Se a lista tiver um tamanho menor ou igual a 1, ela é considerada ordenada e é retornada.

    # middle = len(arr) // 2
    # left_half = arr[:middle]
    # right_half = arr[middle:]
# Calcula o índice do meio da lista e divide a lista em duas partes, criando as sublistas 
# left_half (metade esquerda) e right_half (metade direita).

    # left_half = merge_sort(left_half)
    # right_half = merge_sort(right_half)
# Chama recursivamente a função merge_sort para ordenar as sublistas left_half e right_half

#     return merge(left_half, right_half)
# Retorna o resultado da fusão (merge) das sublistas ordenadas left_half e right_half.

# def merge(left, right):
# Definição da função merge, responsável por combinar duas listas ordenadas (left e right) em 
# uma única lista ordenada

    # result = []
    # left_index, right_index = 0, 0
# Inicializa uma lista vazia result para armazenar os elementos ordenados resultantes da fusão.
# Também cria índices left_index e right_index para rastrear as posições atuais nas listas left
# e right

    # while left_index < len(left) and right_index < len(right):
# Enquanto houver elementos não processados tanto em left quanto em right, realiza o seguinte:

        # if left[left_index] < right[right_index]:
# Verifica se o elemento atual em left é menor do que o elemento atual em right.

            # result.append(left[left_index])
            # left_index += 1
# Se o elemento em left for menor, adiciona-o à lista result e incrementa o índice left_index.

        # else:
        #     result.append(right[right_index])
        #     right_index += 1
# Se o elemento em right for menor ou igual, adiciona-o à lista result e incrementa
# o índice right_index.

    # result.extend(left[left_index:])
    # result.extend(right[right_index:])
# Após sair do laço acima, adiciona os elementos restantes das listas left e right à lista 
# result.

    # return result
# Retorna a lista result, que agora contém todos os elementos mesclados e ordenados.

# O restante do código cria uma lista de números desordenados, aplica o algoritmo Merge Sort
# chamando a função merge_sort e imprime a lista resultante, que estará ordenada.













