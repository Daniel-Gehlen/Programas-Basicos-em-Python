``` mermaid
graph TD
    Start[Início]
    InputPeso[Entrada: peso]
    InputAltura[Entrada: altura]
    CalculateIMC[Calcular IMC]
    OutputIMC[Saída: imc]
    CheckUnderweight[Verificar Abaixo do Peso]
    CheckNormalWeight[Verificar Peso Normal]
    CheckOverweight[Verificar Acima do Peso]
    CheckObesity1[Verificar Obesidade I]
    CheckObesity2[Verificar Obesidade II]
    CheckObesity3[Verificar Obesidade III]
    End[Fim]

    Start --> InputPeso
    InputPeso --> InputAltura
    InputAltura --> CalculateIMC
    CalculateIMC --> OutputIMC
    OutputIMC --> CheckUnderweight
    OutputIMC --> CheckNormalWeight
    OutputIMC --> CheckOverweight
    OutputIMC --> CheckObesity1
    OutputIMC --> CheckObesity2
    OutputIMC --> CheckObesity3
    CheckUnderweight --> |imc < 18.5| End
    CheckNormalWeight --> |18.5 <= imc < 24.9| End
    CheckOverweight --> |25 <= imc < 29.9| End
    CheckObesity1 --> |30 <= imc < 34.9| End
    CheckObesity2 --> |35 <= imc < 39.9| End
    CheckObesity3 --> |ou| End
```