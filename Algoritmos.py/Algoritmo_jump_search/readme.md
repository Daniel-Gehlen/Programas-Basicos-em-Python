``` mermaid
graph TD
  subgraph jump_search_function
    jump_search[jump_search]
    calculate_step[step = in n ** 0.5]
    set_prev[prev = 0]
    block_search["Encontra o bloco"]
    linear_search["Busca linear no bloco"]
  end

  subgraph Exemplo
    arr[[2, 5, 8, 12, 16, 23, 38, 56, 72, 91]]
    target[23]
    result[jump_search]
    print_result["Print resultado"]
  end

  jump_search --> calculate_step
  jump_search --> set_prev
  jump_search --> block_search
  block_search --> linear_search
  linear_search --> result

  calculate_step --> step
  set_prev --> prev
  block_search --> step
  block_search --> prev

  arr --> result
  target --> result
  result --> print_result
```