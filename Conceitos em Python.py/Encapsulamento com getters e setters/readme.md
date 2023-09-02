``` mermaid
classDiagram
  class BankAccount {
    - __account_number: String
    - __balance: float
    + __init__(account_number: String, balance: float): void
    + account_number: String
    + balance: float
    + balance=new_balance: void
    + withdraw(amount: float): void
    + deposit(amount: float): void
  }

  BankAccount "1" --> "1" String: __account_number
  BankAccount "1" --> "1" float: __balance
  BankAccount --|> String
  BankAccount --|> float
```