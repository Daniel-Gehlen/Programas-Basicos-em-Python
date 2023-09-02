``` mermaid
graph TD;
  A --> B;
  A --> C;
  B --> D;
  C --> D;
  subgraph BFS_Process
    A['A' Representa o vertice A]
    B['B' Representa o vertice B]
    C['C' Representa o vertice C]
    D['D' Representa o vertice D] 

    A --> B 
    A --> C
    B --> D
    C --> D
    B --> A
    C --> A
    D --> B
    D --> C
    A -->|Visitado. Aresta entre A e B| B 
    A -->|Visitado| C
    B -->|Visitado| D
    C -->|Visitado| D
    B -->|Visitado| A
    C -->|Visitado. Aresta reversa entre C e A para representar o caminho de volta| A
    D -->|Visitado| B
    D -->|Visitado| C
  end

```