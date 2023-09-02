``` mermaid
graph TD
  start[Start]
  declareClasses[Declare Customer, EmailSender, and CustomerService classes]
  createServiceInstance[Create instance of CustomerService]
  callCreateCustomer[Call create_customer method]
  en[End]

  start --> declareClasses
  declareClasses --> createServiceInstance
  createServiceInstance --> callCreateCustomer
  callCreateCustomer
```