``` mermaid
classDiagram
  class Person {
    - name: String
    - __age: int
    + __init__(name: String, age: int): void
    + get_age(): int
    + set_age(new_age: int): void
  }

  Person "1" --> "1" String: name
  Person "1" --> "1" int: __age
  Person --|> String
  Person --|> int
```