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
print(testelista)

pos = busca_sequncial_ordenada(testelista, 15)
print(15, pos)

pos = busca_sequncial_ordenada(testelista, 13)
print(13, pos)