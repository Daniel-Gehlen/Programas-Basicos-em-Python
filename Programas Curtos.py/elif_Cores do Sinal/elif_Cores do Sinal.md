``` mermaid
graph TD
    Start[Início]
    Input[Entrada de Cor]
    CheckColor[Verificar Cor]
    Accelerate[Acelerar]
    Caution[Atenção]
    Stop[Parar]
    End[Fim]

    Start --> Input
    Input --> CheckColor
    CheckColor --> Accelerate
    CheckColor --> Caution
    CheckColor --> Stop
    Accelerate --> End
    Caution --> End
    Stop --> End
```