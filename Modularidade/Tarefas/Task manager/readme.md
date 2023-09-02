``` mermaid
graph TD
  start[Start]
  importModules[Import task_creation and task_listing modules]
  declareTasks[Declare tasks list]
  mainFunction[Call main function]
  displayMenu[Display Task Manager Menu]
  getUserChoice[Get user choice]
  createTask[Create Task]
  listTasks[List Tasks]
  exitProgram[Exit Program]
  invalidChoice[Invalid Choice]
  e[End]

  start --> importModules
  importModules --> declareTasks
  declareTasks --> mainFunction
  mainFunction --> displayMenu
  displayMenu --> getUserChoice
  getUserChoice --> createTask
  getUserChoice --> listTasks
  getUserChoice --> exitProgram
  createTask --> mainFunction
  listTasks --> mainFunction
  exitProgram --> mainFunction
  invalidChoice --> mainFunction
  mainFunction --> e
```