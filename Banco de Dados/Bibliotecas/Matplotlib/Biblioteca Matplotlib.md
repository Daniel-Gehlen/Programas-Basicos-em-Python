``` mermaid
graph TD
  importMatplotlib[Importar matplotlib.pyplot como plt]
  dados[Dados de exemplo]
  criarGrafico[Criar gráfico de barras]
  definirEixos[Definir rótulos dos eixos e título]
  mostrarGrafico[Mostrar o gráfico]

  importMatplotlib -->|Passo 1| dados
  dados -->|Passo 2| criarGrafico
  criarGrafico -->|Passo 3| definirEixos
  definirEixos -->|Passo 4| mostrarGrafico

```