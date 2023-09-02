``` mermaid
graph TD
  start[Start]
  createDataFrame[Criar DataFrame]
  setIndex[Definir índice personalizado]
  displayOriginal[Exibir DataFrame original]
  displayLoc[Acessar dados com loc]
  displayIloc[Acessar dados com iloc]
  en[End]

  start --> createDataFrame
  createDataFrame --> setIndex
  setIndex --> displayOriginal
  displayOriginal --> displayLoc
  displayLoc --> displayIloc
  displayIloc --> en
```