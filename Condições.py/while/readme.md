``` mermaid
graph TD
  start[Start]
  defineNumber[Definir number: 1]
  loop[Loop]
  getUserInput[Obter entrada do usuário]
  checkZero[Verificar se é zero]
  checkEven[Verificar se é par]
  checkOdd[Verificar se é ímpar]
  en[End]

  start --> defineNumber
  defineNumber --> loop
  loop --> getUserInput
  getUserInput --> checkZero
  checkZero -->|Sim| printEnd
  checkZero -->|Não| checkEven
  printEnd[Imprimir encerramento do programa]
  checkEven -->|Sim| printEven
  checkEven -->|Não| checkOdd
  printEven[Imprimir número par]
  checkOdd -->|Sim| printOdd
  checkOdd -->|Não| loop
  printOdd[Imprimir número ímpar]
  printEnd --> en
```