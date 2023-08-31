def jump_search(arr, target):
    n = len(arr)
    step = int(n ** 0.5)  # Tamanho do salto entre os blocos
    prev = 0
    
    # Encontra o bloco onde o elemento pode estar
    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(n ** 0.5)
        if prev >= n:  # Se o tamanho do salto ultrapassar o tamanho do array
            return -1   # Elemento não encontrado
    
    # Realiza uma busca linear dentro do bloco
    while arr[prev] < target:
        prev += 1
        if prev == min(step, n):  # Se alcançar o próximo bloco ou o final do array
            return -1              # Elemento não encontrado
        if arr[prev] == target:
            return prev  # Elemento encontrado
    
    return -1  # Elemento não encontrado

# Exemplo de uso
arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target = 23
result = jump_search(arr, target)

if result != -1:
    print(f"Elemento {target} encontrado na posição {result}")
else:
    print(f"Elemento {target} não encontrado")

# Neste exemplo, o algoritmo realiza saltos no array de tamanho n utilizando um tamanho de salto
# aproximadamente igual à raiz quadrada de n. Isso ajuda a reduzir o número de comparações necessárias
# em comparação com uma busca linear tradicional.

# Lembre-se de que o algoritmo de busca por saltos só é eficiente em conjuntos de dados ordenados.
# Se o conjunto não estiver ordenado, o resultado não será correto. Além disso, em casos onde 
# o tamanho do conjunto é pequeno, a busca linear tradicional pode ser mais eficiente devido ao 
# overhead dos saltos e comparações adicionais.