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

print(testelista)

pos = busca_sequncial(testelista, 15)

print(15, pos)

pos = busca_sequncial(testelista, 19)

print(19, pos)