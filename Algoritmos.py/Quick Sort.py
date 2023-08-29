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