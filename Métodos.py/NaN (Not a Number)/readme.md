``` mermaid
graph TD
  start[Início]
  importLibraries[Importar bibliotecas]
  createDataFrame[Criar DataFrame]
  checkMissingValues[Verificar valores ausentes]
  dropMissingValues[Remover valores ausentes]
  fillMissingValues[Preencher valores ausentes]
  en[Fim]

  start --> importLibraries
  importLibraries --> createDataFrame
  createDataFrame --> checkMissingValues
  checkMissingValues --> dropMissingValues
  checkMissingValues --> fillMissingValues
  dropMissingValues --> fillMissingValues
  fillMissingValues --> en
  
  createDataFrame --> |Dados| data{"data = {'Nome': ['Alice', 'Bob', 'Carol', 'David'],\n        'Idade': [25, np.nan, 22, 28],\n        'Nota': [90, 75, np.nan, 60]}"}
  checkMissingValues --> |DataFrame booleano| isna{isna}
  dropMissingValues --> |DataFrame sem ausentes| df_sem_ausentes
  fillMissingValues --> |DataFrame preenchido| df_preenchido
```