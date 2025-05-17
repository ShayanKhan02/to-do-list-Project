tasks = [
    {"task": "Buy Milk", "status": "Pending"},
    {"task": "Meeting With colleague", "status": "Done"},
]
def show_menu():
        print("---- To-Do-List ----")
        print("1.Add task")
        print("2.Mark task as Done")
        print("3.View task")
        print("4.Delete task")
        print("5.Update task")
        print("6.Exit")
    
while True:
    show_menu()
    choice = input("Enter the choice (1-4): ")

    if choice == "1":
        task = input("Enter the task: ")
        tasks.append({"task": task, "status": "Pending"})
        print("Task added successfully!")
    elif choice == "2":
        task_num = int(input("Enter task number to mark as done: "))
        if task_num <=len(task):
            tasks[task_num -1]["status"] = "Done"
            print("Task marked as Done!")
        else:
            print("Invalid task number.")
    elif choice == "3":
       if not tasks:
            print("No tasks available.")
       else:
            print("\nTasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task['task']} [{task['status']}]")
    elif choice == "4":
        task_num = int(input("Enter task number to delete: "))
        if 1 <= task_num <= len(tasks):
           deleted = tasks.pop(task_num - 1)
           print(f"Deleted task: {deleted['task']}")
        else:
            print("Invalid task number.")

    elif choice == "5":
        task_num = int(input("Enter the task number to update: "))
        if task_num <= len(tasks):
            new_task = input("Enter the new task: ")
            tasks[task_num -1] = new_task
            print("Task update successfully!")
        else:
            print("Invalid task number.")
    elif choice == "6":
        print("Godd Bye!")
        break
    else:
        print("Invalid choice Try again.")
