``` mermaid
graph TD
  start[Start]
  createData[Criar dados]
  createDataFrame[Criar DataFrame]
  printOriginal[Imprimir DataFrame original]
  selectRows[Selecionar linhas com notas acima de 80]
  printSelected[Imprimir alunos com notas acima de 80]
  en[End]

  start --> createData
  createData --> createDataFrame
  createDataFrame --> printOriginal
  printOriginal --> selectRows
  selectRows --> printSelected
  printSelected
```