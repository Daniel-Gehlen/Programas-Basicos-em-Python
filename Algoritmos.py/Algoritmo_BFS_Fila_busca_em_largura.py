# Vamos supor que temos o seguinte grafo não direcionado:

# A -- B
# |    |
# C -- D

from collections import defaultdict, deque

# Definindo o grafo como um dicionário de listas de adjacência
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}

def bfs(graph, start):
    visited = set()  # Conjunto para armazenar vértices visitados
    queue = deque([start])  # Fila para armazenar os vértices a serem explorados
    
    while queue:
        vertex = queue.popleft()  # Pega o próximo vértice da fila
        if vertex not in visited:
            print(vertex, end=' ')  # Processa o vértice
            visited.add(vertex)
            queue.extend(adjacent for adjacent in graph[vertex] if adjacent not in visited)

# Chama a função BFS com o vértice inicial 'A'
bfs(graph, 'A')


# Explicação do código:

# O grafo é representado como um dicionário de listas de adjacência, onde as chaves são os vértices 
# e os valores são listas de vértices adjacentes.

# A função bfs implementa o algoritmo BFS. Ela começa com o vértice inicial (start) e 
# mantém uma fila de vértices a serem explorados.

# O loop while continua até que a fila esteja vazia. A cada iteração, o vértice na frente da fila
# é removido (popleft) e explorado.

# Se o vértice ainda não foi visitado, ele é processado (neste caso, apenas impresso) 
# e marcado como visitado.

# Os vértices adjacentes ao vértice atual que ainda não foram visitados são adicionados à fila.

# Ao rodar o código com o vértice inicial 'A', ele imprimirá a ordem de visitação dos vértices
# conforme a busca em largura: A, B, C, D. A busca começa pelo vértice 'A', depois explora
# seus vizinhos 'B' e 'C', e finalmente chega ao vértice 'D'.

# Esse é um exemplo simples de busca em largura em um grafo não direcionado. A BFS é amplamente
# utilizada em algoritmos de roteamento, sistemas de navegação, processamento de imagens, jogos e
# muito mais, devido à sua capacidade de encontrar o caminho mais curto entre dois pontos 
# em um grafo.