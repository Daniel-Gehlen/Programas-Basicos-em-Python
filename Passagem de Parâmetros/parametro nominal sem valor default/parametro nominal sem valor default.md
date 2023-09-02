``` mermaid
graph TD
    Start[Início]
    DefFunc[Definir função converter_maiuscula]
    CallFunc[Chamada da função]
    End[Fim]

    Start --> DefFunc
    DefFunc --> CallFunc
    CallFunc --> |Parâmetros| Param{"texto='João', flag_maiuscula=True"}
    CallFunc --> Cond[Condição: flag_maiuscula]
    Cond --> |True| TrueBranch[Verdadeiro]
    TrueBranch --> UpperCall[Chamada de texto.upper]
    Cond --> |False| FalseBranch[Falso]
    FalseBranch --> LowerCall[Chamada de texto.lower]
    UpperCall --> Result["Resultado (texto em maiúsculas)"]
    LowerCall --> Result
    Result --> End

```