``` mermaid
graph TD
    Start[Início]
    Input[Entrada de Login e Senha]
    CheckUser[Verificar Usuário e Senha]
    Welcome[Exibir Mensagem de Boas-Vindas]
    Failed[Exibir Mensagem de Falha]
    End[Fim]

    Start --> Input
    Input --> CheckUser
    CheckUser --> Welcome
    CheckUser --> Failed
    Welcome --> End
    Failed --> End
```