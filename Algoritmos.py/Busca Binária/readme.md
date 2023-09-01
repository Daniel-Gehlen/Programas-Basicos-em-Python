``` mermaid
graph TD
  subgraph BuscadorClass
    Buscador[Buscador]
    busca_sequencial[busca_sequencial]
    busca_binaria[busca_binaria]
  end

  subgraph Exemplo
    lista[[-200, 4, 50, 333]]
    b[Buscador]
    busca_binaria[busca_binaria]
    print_result["Print resultado"]
  end

  Buscador --> busca_sequencial
  Buscador --> busca_binaria
  busca_binaria --> primeiro
  busca_binaria --> ultimo
  busca_binaria --> meio
  busca_binaria --> comparacao
  comparacao --> resultado
  busca_sequencial --> lista
  busca_sequencial --> x
  busca_sequencial --> resultado
  lista --> busca_binaria
  b --> busca_binaria
  busca_binaria --> print_result
```