tasks = []
print("Welcome to the To do List for Productivity")

def create_task():
    task = input("Enter your task for the fruitful day!: ")
    tasks.append(task)
    print("Task saved in todo's mind successfully!")

def view_tasks():
    if not tasks:
        print("No tasks available. To do is sad")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def delete_task():
    view_tasks()
    task_index = int(input("Enter task number to delete: ")) - 1
    if task_index >= 0 and task_index < len(tasks):
        del tasks[task_index]
        print("Task deleted successfully!")
    else:
        print("Invalid task number.")

while True:
    print("\nTodo List Menu:")
    print("1. Create Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Quit")
    choice = input("Enter your choice (1/2/3/4): ")
    if choice == "1":
        create_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        print("Thank you")
        break
    else:
        print("Invalid choice. Please choose a valid option sweetheart")
