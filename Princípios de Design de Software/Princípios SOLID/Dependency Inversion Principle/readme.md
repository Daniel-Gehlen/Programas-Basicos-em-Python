``` mermaid
graph TD
  start[Start]
  declareClasses[Declare LightBulb, Switchable, Switch, and ElectricSocket classes]
  createInstances[Create instances of LightBulb, ElectricSocket, and Switch]
  callFunction[Call switch.operate]
  displayResult[Display operation result]
  e[End]

  start --> declareClasses
  declareClasses --> createInstances
  createInstances --> callFunction
  callFunction --> displayResult
  displayResult
```