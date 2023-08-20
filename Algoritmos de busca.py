# Algoritmo de busca sequêncial while

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

print(busca_sequencial(testelista, 5)):
print(busca_sequencial(testelista, 15))
        

# Busca sequencial ordenada
def busca_sequncial_ordenada(lista, elemento):
    pos = 0
    encontrado = False
    para = False

    while pos < len(lista) and not encontrado and not para:
        if lista[pos] == elemento:
            encontrado = True
        else:
            if lista[pos] > elemento:
                para = True 
            pos = pos+1

    return encontrado

testelista = [2, 10, 8, 15, 18, 20, 12, 1]
print(busca_sequencial(testelista, 5))
print(busca_sequencial(testelista, 15))

# Algoritmo de busca binária
def busca_binaria(lista, elemento):
    minimo = len(lista)-1
    encontrado = False

    while minimo <= maximo and not encontrado:
        meio_lista = (minimo + maximo)//2
        if lista[meio_lista] == elemento:
            encontrado = True
        else:
            if elemento < lista[meio_lista]:

                maximo = meio_lista - 1

            else:
                minimo = meio_lista+1

    return encontrado

testelista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(busca_binaria(testelista, 14))

# Algoritmo de ordenação por inserção (selection sort)
for i in (1 > 6):
    j = i - 1
    while (j >= 0) and (a[j]) > (a[j+1]):
        swap (a[j]) (a[j+1])
        j = j-1

# Algoritmo de ordenação por bolha (bubble sort)
# Algoritmo de ordenação merge sort (dividir para conquistar)
# Algoritmo de ordenação quick sort

