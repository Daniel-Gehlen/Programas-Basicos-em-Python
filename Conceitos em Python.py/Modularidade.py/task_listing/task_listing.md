``` mermaid
graph TD
  start[Start]
  declareTasks[Declare tasks list]
  callFunction[Call list_tasks function]
  listTasks[list_tasks function]
  iterateList[Iterate through tasks list]
  determineStatus[Determine task status]
  printTask[Print task information]
  e[End]

  start --> declareTasks
  declareTasks --> callFunction
  callFunction --> listTasks
  listTasks --> iterateList
  iterateList --> determineStatus
  determineStatus --> printTask
  printTask --> iterateList
  iterateList
  e[End]
```