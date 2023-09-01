``` mermaid
graph TD
  subgraph GrafoClass
    Grafo[Grafo]
    __init__[__init__]
    adicionar_vertice[adicionar_vertice]
    adicionar_aresta[adicionar_aresta]
    dfs[dfs]
    busca_em_profundidade[busca_em_profundidade]
  end

  subgraph Exemplo
    grafo_exemplo[Grafo]
    adicionar_vertice1[adicionar_vertice 1]
    adicionar_vertice2[adicionar_vertice 2]
    adicionar_vertice3[adicionar_vertice 3]
    adicionar_vertice4[adicionar_vertice 4]
    adicionar_vertice5[adicionar_vertice 5]
    adicionar_aresta1[adicionar_aresta 1 2]
    adicionar_aresta2[adicionar_aresta 1 3]
    adicionar_aresta3[adicionar_aresta 2 4]
    adicionar_aresta4[adicionar_aresta 2 5]
    busca_em_profundidade[busca_em_profundidade 1]
  end

  Grafo --> __init__
  Grafo --> adicionar_vertice
  Grafo --> adicionar_aresta
  Grafo --> dfs
  Grafo --> busca_em_profundidade

  grafo_exemplo --> Grafo
  adicionar_vertice1 --> grafo_exemplo
  adicionar_vertice2 --> grafo_exemplo
  adicionar_vertice3 --> grafo_exemplo
  adicionar_vertice4 --> grafo_exemplo
  adicionar_vertice5 --> grafo_exemplo
  adicionar_aresta1 --> grafo_exemplo
  adicionar_aresta2 --> grafo_exemplo
  adicionar_aresta3 --> grafo_exemplo
  adicionar_aresta4 --> grafo_exemplo
  busca_em_profundidade --> grafo_exemplo
```