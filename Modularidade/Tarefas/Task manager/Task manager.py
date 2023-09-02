# Vamos supor que estamos construindo um sistema de gerenciamento de tarefas, e queremos dividir
# nosso código em módulos para lidar com a criação, listagem e conclusão de tarefas.

# Vamos criar três módulos: task_manager.py, task_creation.py e task_listing.py. 
#Cada um desses módulos terá responsabilidades específicas dentro do sistema.

#Módulo task_creation.py (Responsável por criar novas tarefas):

# task_creation.py

# def create_task(tasks, task_name):
#     tasks.append({"name": task_name, "completed": False})
#     print(f"Task '{task_name}' created successfully.")

# if __name__ == "__main__":
#     tasks = []
#     task_name = input("Enter task name: ")
#     create_task(tasks, task_name)

# #Módulo task_listing.py (Responsável por listar as tarefas existentes):

# def list_tasks(tasks):
#     print("Task List:")
#     for idx, task in enumerate(tasks, start=1):
#         status = "Completed" if task["completed"] else "Incomplete"
#         print(f"{idx}. {task['name']} - {status}")

# if __name__ == "__main__":
#     tasks = [{"name": "Example Task 1", "completed": False}, {"name": "Example Task 2", "completed": True}]
#     list_tasks(tasks)

# Módulo task_manager.py (Módulo principal que utiliza os outros módulos):

# task_manager.py

import task_creation
import task_listing

def main():
    tasks = []
    
    while True:
        print("\nTask Manager Menu:")
        print("1. Create Task")
        print("2. List Tasks")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            task_name = input("Enter task name: ")
            task_creation.create_task(tasks, task_name)
        elif choice == "2":
            task_listing.list_tasks(tasks)
        elif choice == "3":
            print("Exiting Task Manager.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
