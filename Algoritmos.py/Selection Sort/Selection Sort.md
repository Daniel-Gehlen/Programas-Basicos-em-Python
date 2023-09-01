``` mermaid
graph TD
  subgraph SelectionSortFunction
    selection_sort[selection_sort]
    outer_loop["Loop Externo"]
    inner_loop["Loop Interno"]
    min_index_assignment["Atribuição de min_index"]
    swap["Troca de Valores"]
  end

  subgraph Exemplo
    numbers[[64, 34, 25, 12, 22]]
    sorted_numbers[selection_sort]
    print_result["Print Lista ordenada"]
  end

  selection_sort --> outer_loop
  outer_loop --> inner_loop
  inner_loop --> min_index_assignment
  min_index_assignment --> swap
  swap --> inner_loop
  outer_loop --> swap

  numbers --> sorted_numbers
  sorted_numbers --> print_result
```