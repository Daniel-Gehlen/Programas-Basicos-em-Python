``` mermaid
classDiagram
  class Author {
    - name: String
    - birth_year: Integer
    - books: List<Book>
    + add_book(book: Book): void
  }
  class Book {
    - title: String
    - year: Integer
    - author: Author
  }

  Author "1" -- "*" Book : writes
```