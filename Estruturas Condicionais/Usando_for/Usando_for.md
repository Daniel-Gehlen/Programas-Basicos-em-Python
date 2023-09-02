``` mermaid
graph TD
  start[Start]
  defineName1[Definir name: 'Guido']
  loop1[Loop]
  printChar1[Imprimir caractere]
  checkNextChar1[Verificar próximo caractere]
  defineName2[Definir name: 'Guido']
  defineCounter[Definir contador: 0]
  loop2[Loop]
  printIndexChar[Imprimir índice e caractere]
  checkNextChar2[Verificar próximo caractere]
  defineName3[Definir name: 'Guido']
  loop3[Loop]
  printNumber[Imprimir número]
  defineDisciplina[Definir disciplina: 'Linguagem de Programação']
  loopBreak[Loop com break]
  printCharBreak[Imprimir caractere]
  checkNextCharBreak[Verificar próximo caractere]
  loopContinue[Loop com continue]
  printCharContinue[Imprimir caractere]
  checkNextCharContinue[Verificar próximo caractere]
  e[End]

  start --> defineName1
  defineName1 --> loop1
  loop1 --> printChar1
  printChar1 --> checkNextChar1
  checkNextChar1 -->|Sim| loop1
  checkNextChar1 -->|Não| defineName2
  defineName2 --> defineCounter
  defineCounter --> loop2
  loop2 --> printIndexChar
  printIndexChar --> checkNextChar2
  checkNextChar2 -->|Sim| loop2
  checkNextChar2 -->|Não| defineName3
  defineName3 --> loop3
  loop3 --> printNumber
  printNumber --> defineDisciplina
  defineDisciplina --> loopBreak
  loopBreak --> printCharBreak
  printCharBreak --> checkNextCharBreak
  checkNextCharBreak -->|Sim| loopBreak
  checkNextCharBreak -->|Não| loopContinue
  loopContinue --> printCharContinue
  printCharContinue --> checkNextCharContinue
  checkNextCharContinue -->|Sim| loopContinue
  checkNextCharContinue -->|Não| en
```