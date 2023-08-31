class Grafo:
    def __init__(self):
        self.grafo = {}

    def adicionar_vertice(self, vertice):
        if vertice not in self.grafo:
            self.grafo[vertice] = []

    def adicionar_aresta(self, vertice1, vertice2):
        self.grafo[vertice1].append(vertice2)
        self.grafo[vertice2].append(vertice1)

    def dfs(self, vertice, visitados):
        visitados.add(vertice)
        print(vertice, end=" ")

        for vizinho in self.grafo[vertice]:
            if vizinho not in visitados:
                self.dfs(vizinho, visitados)

    def busca_em_profundidade(self, vertice_inicial):
        visitados = set()
        self.dfs(vertice_inicial, visitados)

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

print("Busca em Profundidade a partir do vértice 1:")
grafo_exemplo.busca_em_profundidade(1)


#Busca em profundidade (DFS) em um grafo não-direcionado usando uma abordagem recursiva:

# Neste exemplo, a classe Grafo representa um grafo não-direcionado utilizando um dicionário, 
# onde as chaves são os vértices e os valores são listas de vértices vizinhos. 
# O método dfs realiza a busca em profundidade de forma recursiva, explorando os vértices vizinhos 
# não visitados de cada vértice.

# O código cria um grafo de exemplo com cinco vértices e quatro arestas, e então executa 
# uma busca em profundidade a partir do vértice 1, exibindo a sequência de vértices visitados.

# A busca em profundidade é uma estratégia de exploração de grafos que começa em um 
# vértice inicial, explora ao máximo um ramo antes de retroceder. É importante notar que 
# a abordagem recursiva pode levar a problemas de estouro de pilha em grafos muito grandes
# ou profundos. Em casos assim, é recomendado utilizar uma abordagem iterativa com o uso de uma
# pilha