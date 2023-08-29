def selection_sort(arr):
    if not arr:
        return arr
    for i in range(len(arr)):
        min_i = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_i]:
                min_i = j
        arr[i], arr[min_i] = arr[min_i], arr[i]

    return arr

# Lista de números desordenados
numbers = [64, 34, 25, 12, 22]

# Chamando a função de ordenação por seleção
sorted_numbers = selection_sort(numbers)

# Imprimindo a lista ordenada
print("Lista ordenada:", sorted_numbers)

    