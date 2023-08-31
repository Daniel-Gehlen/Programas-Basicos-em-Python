def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

# Exemplo de uso
sorted_list = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
target_element = 10

result = binary_search(sorted_list, target_element)
if result != -1:
    print(f'O elemento {target_element} foi encontrado no índice {result}.')
else:
    print(f'O elemento {target_element} não foi encontrado na lista.')

#Explicação:

# A função binary_search recebe uma lista ordenada (arr) e o elemento que estamos procurando (target).
# Inicializamos dois ponteiros, left e right, que representam os índices extremos da parte do array 
# que estamos considerando.
# Entramos em um loop enquanto left for menor ou igual a right.
# Dentro do loop, calculamos o índice do meio (mid) usando a média entre left e right. 
# Isso nos permite dividir o intervalo ao meio.
# Comparamos o elemento no índice mid com o elemento que estamos procurando (target).
# Se forem iguais, retornamos o índice mid, pois encontramos o elemento.
# Se o elemento no índice mid for menor que target, sabemos que o elemento que procuramos está
# à direita de mid, então atualizamos left para mid + 1.
# Se o elemento no índice mid for maior que target, sabemos que o elemento que procuramos está 
# à esquerda de mid, então atualizamos right para mid - 1.
# Se o loop terminar sem encontrar o elemento, retornamos -1 para indicar que o elemento 
# não está na lista.
# A busca binária é altamente eficiente em conjuntos de dados ordenados, 
# pois a cada iteração ela reduz pela metade o tamanho do intervalo em que o elemento pode estar.
# Isso leva a um desempenho muito bom, com complexidade no pior caso de O(log n), 
# o que a torna uma escolha excelente para conjuntos de dados grandes.