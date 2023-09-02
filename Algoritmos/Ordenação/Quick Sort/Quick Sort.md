``` mermaid
graph TD
  subgraph QuickSortFunction
    quick_sort[quick_sort]
    choose_pivot[Escolher Pivot]
    divide[Dividir em 3 Partes]
    recursive_left[Chamar quick_sort  Esquerda]
    recursive_right[Chamar quick_sort  Direita]
    combine[Combinar Subarrays]
    return[Retornar Array Ordenado]
  end

  subgraph Exemplo
    numbers[[64, 34, 25, 12, 22]]
    sorted_numbers[quick_sort]
    print_result[Print Lista ordenada]
  end

  quick_sort --> choose_pivot
  choose_pivot --> divide
  divide --> recursive_left
  divide --> recursive_right
  recursive_left --> quick_sort
  recursive_right --> quick_sort
  recursive_left --> combine
  recursive_right --> combine
  combine --> return

  numbers --> sorted_numbers
  sorted_numbers --> print_result
```