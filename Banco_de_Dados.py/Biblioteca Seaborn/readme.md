``` mermaid
flowchart TD
  importSeaborn[Importar seaborn como sns]
  importMatplotlib[Importar matplotlib.pyplot como plt]
  dados[Dados de exemplo]
  configurarEstilo[Configurar estilo]
  criarGrafico[Criar gráfico de dispersão com regressão]
  definirEixos[Definir rótulos dos eixos e título]
  mostrarGrafico[Mostrar o gráfico]

  importSeaborn --> importMatplotlib --> dados --> configurarEstilo --> criarGrafico --> definirEixos --> mostrarGrafico

```