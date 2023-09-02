``` mermaid
graph TD
  start[Start]
  defineValues[Definir valores: valor1=10, valor2=20]
  checkCondition[Verificar condição]
  printResult1[Imprimir 'valor1 é maior que valor2']
  printResult2[Imprimir 'valor2 é maior que valor1']
  e[End]

  start --> defineValues
  defineValues --> checkCondition
  checkCondition -->|Sim| printResult1
  checkCondition -->|Não| printResult2
  printResult1 --> 
  printResult2
```