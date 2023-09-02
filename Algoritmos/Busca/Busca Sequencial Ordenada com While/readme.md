``` mermaid
graph TD
  subgraph BuscaSequencialFunction
    busca_sequencial[busca_sequencial]
    while_loop["While loop"]
    check_condition["Verifica condição"]
    update_position["Atualiza posição"]
  end

  subgraph Exemplo
    testelista[[2, 10, 8, 15, 18, 20, 12, 1]]
    pos1[busca_sequencial]
    print_result1["Print resultado 15"]
    pos2[busca_sequencial]
    print_result2["Print resultado 19"]
  end

  busca_sequencial --> while_loop
  while_loop --> check_condition
  while_loop --> update_position
  check_condition --> resultado
  update_position --> pos
  pos --> print_result1
  pos --> print_result2

  testelista --> pos1
  15 --> pos1
  pos1 --> print_result1

  testelista --> pos2
  19 --> pos2
  pos2 --> print_result2
```