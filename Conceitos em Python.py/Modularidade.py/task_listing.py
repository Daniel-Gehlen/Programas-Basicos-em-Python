# #Módulo task_listing.py (Responsável por listar as tarefas existentes):

def list_tasks(tasks):
    print("Task List:")
    for idx, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Incomplete"
        print(f"{idx}. {task['name']} - {status}")

if __name__ == "__main__":
    tasks = [{"name": "Example Task 1", "completed": False}, {"name": "Example Task 2", "completed": True}]
    list_tasks(tasks)