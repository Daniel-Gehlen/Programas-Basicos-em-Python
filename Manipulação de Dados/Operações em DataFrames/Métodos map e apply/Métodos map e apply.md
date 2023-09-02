``` mermaid
graph TD
  start[Início]
  importLibraries[Importar bibliotecas]
  createDataFrame[Criar DataFrame]
  createMapping[Criar dicionário de códigos de países]
  useMap[Usar o método map]
  useApply[Usar o método apply]
  en[Fim]

  start --> importLibraries
  importLibraries --> createDataFrame
  createDataFrame --> createMapping
  createMapping --> useMap
  useMap --> useApply
  useApply --> en
  
  createDataFrame --> |Dados| data -->
  dataPaís['Brasil', 'Estados Unidos', 'Canadá', 'México']
  createMapping --> |Códigos| codigo -->
  Paises['Brasil': 'BR', 'Estados Unidos': 'US', 'Canadá': 'CA', 'México': 'MX']
  useMap --> |Nova coluna 'Código'| df --> codigo['Código']
  useApply --> |Nova coluna 'Comprimento'| df --> Comprimento['Comprimento']
```