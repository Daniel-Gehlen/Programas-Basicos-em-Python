``` mermaid
graph TD
    Start[Início]
    DefFunc[Definir função somar]
    CallFunc[Chamada da função somar]
    End[Fim]

    Start --> DefFunc
    DefFunc --> CallFunc
    CallFunc --> |Parâmetros| Param{"a=2, b=3"}
    Param --> Add[Realizar soma]
    Add --> Result["Resultado (r)"]
    CallFunc --> Result
    Result --> Print[Imprimir resultado]
    Print --> End
```