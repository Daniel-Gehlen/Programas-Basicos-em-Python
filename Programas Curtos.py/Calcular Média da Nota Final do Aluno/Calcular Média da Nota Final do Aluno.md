``` mermaid
graph TD
    Start[Início]
    InputFaltas[Entrada: qtdade_faltas]
    InputMedia[Entrada: media_final]
    Check[Verificar condições]
    Approve[Aluno aprovado]
    Reprove[Aluno reprovado]
    End[Fim]

    Start --> InputFaltas
    InputFaltas --> Check
    InputMedia --> Check
    Check --> |qtdade_faltas <= 5 && media_final >= 7| Approve
    Check --> |ou| Reprove
    Approve --> End
    Reprove --> End
```