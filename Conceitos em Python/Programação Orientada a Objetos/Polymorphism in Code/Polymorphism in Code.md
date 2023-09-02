``` mermaid
graph TD
  start[Start]
  declareClasses[Declare Animal, Dog, Cat, and Cow classes]
  declareFunction[Declare animal_sound function]
  createInstances[Create instances of Dog, Cat, and Cow]
  callFunction1[Call animal_sound dog]
  callFunction2[Call animal_soundcat]
  callFunction3[Call animal_sound cow]
  displayResults[Display sound results]
  e[End]

  start --> declareClasses
  declareClasses --> declareFunction
  declareFunction --> createInstances
  createInstances --> callFunction1
  createInstances --> callFunction2
  createInstances --> callFunction3
  callFunction1 --> displayResults
  callFunction2 --> displayResults
  callFunction3 --> displayResults
  displayResults
```