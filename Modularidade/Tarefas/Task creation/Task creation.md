``` mermaid
graph TD
  start[Start]
  declareTasks[Declare tasks list]
  getInput[Get input for task name]
  callFunction[Call create_task function]
  createTask[create_task function]
  modifyList[Modify tasks list]
  printResult[Print success message]


  start --> declareTasks
  declareTasks --> getInput
  getInput --> callFunction
  callFunction --> createTask
  createTask --> modifyList
  modifyList --> printResult
```