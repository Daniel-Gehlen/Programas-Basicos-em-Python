``` mermaid
classDiagram
  class Usuario {
    - nome: String
    - idade: Integer
    - email: String
    - livros_emprestados: List<Livro>
    + emprestar_livro(livro: Livro): void
    + devolver_livro(livro: Livro): void
  }
  class Livro {
    - titulo: String
    - autor: String
    - emprestado_para: Usuario
  }
  
  Usuario "1" *-- "3..*" Livro : empresta/devolve
```