``` mermaid
graph TD
  somar[somar = lambda x, y: x + y]
  resultado[resultado = somar x=5, y=3]
  imprimir[print f Resultado da soma: resultado]

  somar --> resultado
  resultado --> imprimir

```