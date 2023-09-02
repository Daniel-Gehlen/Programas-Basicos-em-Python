``` mermaid
graph TD
  start[Start]
  declareClasses[Declare Worker, Manager, Employee, and Supervisor classes]
  createInstances[Create instances of Employee and Supervisor]
  callFunctions[Call employee.work, supervisor.work, and supervisor.manage]
  displayResults[Display work and management results]
  e[End]

  start --> declareClasses
  declareClasses --> createInstances
  createInstances --> callFunctions
  callFunctions --> displayResults
  displayResults --> e
```