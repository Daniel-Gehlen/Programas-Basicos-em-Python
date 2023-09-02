``` mermaid
graph TD
  start[Início]
  importLibraries[Importar bibliotecas]
  createNumericData[Criar dados numéricos]
  createHistogram[Criar histograma]
  showHistogram[Mostrar histograma]
  createCategoricalData[Criar dados categóricos]
  createBarChart[Criar gráfico de barras]
  showBarChart[Mostrar gráfico de barras]
  en[Fim]

  start --> importLibraries
  importLibraries --> createNumericData
  createNumericData --> createHistogram
  createHistogram --> showHistogram
  showHistogram --> createCategoricalData
  createCategoricalData --> createBarChart
  createBarChart --> showBarChart
  showBarChart
  
  createNumericData --> |Dados numéricos| data[val1, val2, ..., val1000]
  createHistogram --> |Bordas| bins{bins = 20}
  createCategoricalData --> |Categorias| categories['A', 'B', 'C', 'D', 'E']
  createCategoricalData --> |Contagens| counts[25, 40, 15, 30, 10]


```