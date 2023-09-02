``` mermaid
graph TD
  start[Start]
  declareClasses[Declare Shape, Rectangle, Circle, and AreaCalculator classes]
  createInstances[Create instances of Rectangle and Circle]
  callFunctions[Call calculate_area with rectangle and circle instances]
  displayResults[Display calculated areas]
  e[End]

  start --> declareClasses
  declareClasses --> createInstances
  createInstances --> callFunctions
  callFunctions --> displayResults
  displayResults
```