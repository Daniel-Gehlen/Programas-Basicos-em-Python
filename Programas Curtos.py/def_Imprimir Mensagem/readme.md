``` mermaid
graph TD
    Start[Início]
    CallFunction[Chamada da Função]
    Function[Função imprimir_mensagem]
    PrintMensagem[Imprimir Mensagem]
    End[Fim]

    Start --> CallFunction
    CallFunction --> Function
    Function --> PrintMensagem
    PrintMensagem --> End
```