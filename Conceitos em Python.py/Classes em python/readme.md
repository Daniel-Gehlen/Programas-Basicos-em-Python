``` mermaid
classDiagram
  class ClassName {
    - _Statement: None
  }

  class PrimeiraClasse {
    - nome: None
    + imprimir_mensagem(): void
  }

  class FuncionarioTecnico {
    - status: String
    + __init__(status: String): void
  }

  ClassName --|> PrimeiraClasse
  PrimeiraClasse --|> FuncionarioTecnico
```