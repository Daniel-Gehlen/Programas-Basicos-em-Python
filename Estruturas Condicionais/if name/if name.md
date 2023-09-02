``` mermaid
graph TD
  start[Start]
  defineName[Definir name: 'Daniel']
  defineLastName[Definir last_name: '']
  defineList[Definir list: vazio]
  checkCondition[Verificar condição]
  printResult[Imprimir 'a variável name não é vazia']
  en[End]

  start --> defineName
  defineName --> defineLastName
  defineLastName --> defineList
  defineList --> checkCondition
  checkCondition -->|Sim| printResult
  printResult
```