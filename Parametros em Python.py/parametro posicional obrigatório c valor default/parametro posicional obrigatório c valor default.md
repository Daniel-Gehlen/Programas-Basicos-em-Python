``` mermaid
graph TD
    Start[Início]
    DefFunc[Definir função calcular_desconto]
    CallFunc1[Chamada da função sem desconto]
    CallFunc2[Chamada da função com desconto]
    End[Fim]

    Start --> DefFunc
    DefFunc --> CallFunc1
    CallFunc1 --> |Parâmetros| Param1{"valor=100, desconto=0"}
    Param1 --> Calculo1[Realizar cálculo]
    Calculo1 --> Result1["Resultado (valor1)"]
    CallFunc1 --> Result1
    DefFunc --> CallFunc2
    CallFunc2 --> |Parâmetros| Param2{"valor=100, desconto=0.25"}
    Param2 --> Calculo2[Realizar cálculo]
    Calculo2 --> Result2["Resultado (valor2)"]
    CallFunc2 --> Result2
    Result1 --> Print1[Imprimir valor1]
    Result2 --> Print2[Imprimir valor2]
    Print1 --> End
    Print2 --> End
```