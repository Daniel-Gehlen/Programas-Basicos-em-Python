#Módulo task_creation.py (Responsável por criar novas tarefas):

# task_creation.py

def create_task(tasks, task_name):
    tasks.append({"name": task_name, "completed": False})
    print(f"Task '{task_name}' created successfully.")

if __name__ == "__main__":
    tasks = []
    task_name = input("Enter task name: ")
    create_task(tasks, task_name)