``` mermaid
graph TD
  declareList[vogais = 'a', 'e', 'i', 'o', 'u']
  appendList[Adicionar elementos à lista vogais]
  accessList[Acessar itens da lista]
  listComprehension[Usar list comprehension]
  tupleDeclaration[Declaração de tupla]
  setDeclaration[Declaração de conjunto set]
  dictDeclaration[Declaração de dicionário]
  modifyDictionary[Modificar valor do dicionário]
  printResult[Imprimir resultado]

  declareList --> appendList
  appendList --> accessList
  accessList -->|Indexing| printResult
  accessList -->|Slicing| printResult
  appendList --> listComprehension
  listComprehension --> printResult
  listComprehension -->|List Comprehension| printResult
  tupleDeclaration --> setDeclaration
  setDeclaration --> dictDeclaration
  dictDeclaration --> modifyDictionary
  modifyDictionary --> printResult
  printResult -->|Print| printResult


```