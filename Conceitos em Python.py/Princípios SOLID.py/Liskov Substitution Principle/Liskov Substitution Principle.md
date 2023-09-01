``` mermaid
graph TD
  start[Start]
  declareClasses[Declare Bird, Sparrow, and Ostrich classes]
  createInstances[Create instances of Sparrow and Ostrich]
  callFunctions[Call bird_in_action with sparrow and ostrich instances]
  displayResults[Display bird actions]
  e[End]

  start --> declareClasses
  declareClasses --> createInstances
  createInstances --> callFunctions
  callFunctions --> displayResults
  displayResults 
```