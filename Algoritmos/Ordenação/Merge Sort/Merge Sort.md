``` mermaid
graph TD

subgraph MergeSortFunction
    merge_sort[merge_sort]
    merge[merge]
    recursive_call_left[Chamada Recursiva  Esquerda]
    recursive_call_right[Chamada Recursiva Direita]
    merge_call[Chamada da Função merge]
end

subgraph Exemplo
    numbers[[64, 34, 25, 12, 22]]
    sorted_numbers[merge_sort]
    print_result[Print Lista ordenada]
end

mergeSort --> recursiveCallLeft
mergeSort --> recursiveCallRight
recursiveCallLeft --> mergeCall
recursiveCallRight --> mergeCall
mergeCall --> merge

merge --> result
merge --> left_index
merge --> right_index

numbers --> sorted_numbers
sorted_numbers --> print_result


```