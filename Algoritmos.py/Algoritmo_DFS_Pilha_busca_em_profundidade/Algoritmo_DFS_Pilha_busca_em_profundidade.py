class Grafo:
    def __init__(self):
        self.grafo = {}

    def adicionar_vertice(self, vertice):
        if vertice not in self.grafo:
            self.grafo[vertice] = []

    def adicionar_aresta(self, vertice1, vertice2):
        self.grafo[vertice1].append(vertice2)
        self.grafo[vertice2].append(vertice1)

    def busca_em_profundidade_iterativa(self, vertice_inicial):
        visitados = set()
        pilha = [vertice_inicial]

        while pilha:
            vertice_atual = pilha.pop()
            if vertice_atual not in visitados:
                print(vertice_atual, end=" ")
                visitados.add(vertice_atual)
                pilha.extend(vizinho for vizinho in self.grafo[vertice_atual] if vizinho not in visitados)

# Criando um grafo de exemplo
grafo_exemplo = Grafo()
grafo_exemplo.adicionar_vertice(1)
grafo_exemplo.adicionar_vertice(2)
grafo_exemplo.adicionar_vertice(3)
grafo_exemplo.adicionar_vertice(4)
grafo_exemplo.adicionar_vertice(5)

grafo_exemplo.adicionar_aresta(1, 2)
grafo_exemplo.adicionar_aresta(1, 3)
grafo_exemplo.adicionar_aresta(2, 4)
grafo_exemplo.adicionar_aresta(2, 5)

print("Busca em Profundidade (iterativa) a partir do vértice 1:")
grafo_exemplo.busca_em_profundidade_iterativa(1)

# Nesta abordagem, a pilha é utilizada para controlar os vértices a serem visitados. 
# O algoritmo começa com o vértice inicial na pilha. Enquanto a pilha não estiver vazia, 
# o vértice atual é retirado da pilha, visitado (se ainda não foi), e seus vizinhos não visitados
# são adicionados à pilha. Esse processo continua até que a pilha esteja vazia, o que significa 
# que todos os vértices alcançáveis a partir do vértice inicial foram visitados.

# Esta abordagem iterativa é mais eficiente em termos de uso de memória em comparação com 
# a abordagem recursiva, especialmente para grafos muito grandes ou profundos.