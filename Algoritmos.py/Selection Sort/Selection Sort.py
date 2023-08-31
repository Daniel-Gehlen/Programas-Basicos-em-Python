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

    
# A definição da função selection_sort(arr) define uma função que irá ordenar a lista de entrada
# arr usando o algoritmo de ordenação por seleção.

# O bloco if not arr: verifica se a lista arr está vazia. Se estiver vazia, a função retorna 
# a lista original, pois não há elementos para ordenar.

# O loop for i in range(len(arr)): percorre todos os índices da lista arr.

# A linha min_i = i inicializa uma variável min_i com o índice atual i, que representa 
# a posição do elemento mínimo no subarray não ordenado.

# O segundo loop for j in range(i + 1, len(arr)): itera sobre os índices após o índice atual i,
# ou seja, percorre os elementos restantes no subarray não ordenado.

# O bloco if arr[j] < arr[min_i]: verifica se o elemento atual arr[j] é menor que 
# o elemento mínimo atual arr[min_i].

# Se o elemento atual for menor, a linha min_i = j atualiza o índice do elemento mínimo para
# o índice j.

# A linha arr[i], arr[min_i] = arr[min_i], arr[i] troca o elemento na posição i com o elemento
# mínimo encontrado, garantindo que o elemento mínimo seja colocado na posição correta.

# O loop externo continua, repetindo o processo para o próximo elemento não ordenado.

# Uma vez que todos os elementos foram percorridos e colocados em suas posições corretas, 
# a função retorna a lista ordenada.

# A lista de números desordenados é definida.

# A função selection_sort() é chamada com a lista numbers e o resultado é atribuído a 
# sorted_numbers.

# A linha print("Lista ordenada:", sorted_numbers) imprime a lista ordenada na saída.