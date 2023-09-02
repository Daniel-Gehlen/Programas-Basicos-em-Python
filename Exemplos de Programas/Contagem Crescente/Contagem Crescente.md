``` mermaid
graph TD
    Start[Início]
    LoopFor[Loop For]
    PrintFor[Imprimir Contagem]
    EndFor[Fim do Loop For]
    LoopWhile[Loop While]
    PrintWhile[Imprimir Contagem]
    Increment[Incrementar Contagem]
    EndWhile[Fim do Loop While]
    End[Fim]

    Start --> LoopFor
    LoopFor --> PrintFor
    PrintFor --> LoopFor
    LoopFor --> EndFor
    EndFor --> LoopWhile
    LoopWhile --> PrintWhile
    PrintWhile --> Increment
    Increment --> LoopWhile
    Increment --> EndWhile
    EndWhile --> End
```