``` mermaid
graph TD
    Start[Início]
    InputA[Entrada de a]
    InputB[Entrada de b]
    BuildEquation[Construir Equação]
    PrintEquation[Imprimir Equação]
    LoopStart[Início do Loop]
    EvaluateEquation[Avaliar Equação]
    PrintResult[Imprimir Resultado]
    LoopEnd[Fim do Loop]
    End[Fim]

    Start --> InputA
    InputA --> InputB
    InputB --> BuildEquation
    BuildEquation --> PrintEquation
    PrintEquation --> LoopStart
    LoopStart --> EvaluateEquation
    EvaluateEquation --> PrintResult
    PrintResult --> LoopEnd
    LoopEnd --> LoopStart
    LoopEnd --> End
    LoopStart --> End
```