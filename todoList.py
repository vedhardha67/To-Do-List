# To-Do List

tasks = []


def add_task(task):
    tasks.append(task)
    print("Task added successfully.")


def view_tasks():
    if len(tasks) == 0:
        print("No tasks found.")
    else:
        print("Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")


def delete_task(task_index):
    if task_index >= 1 and task_index <= len(tasks):
        deleted_task = tasks.pop(task_index - 1)
        print(f"Deleted task: {deleted_task}")
    else:
        print("Invalid task index.")


def main():
    while True:
        print("\n===== TO-DO LIST =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            task = input("Enter task: ")
            add_task(task)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            task_index = int(input("Enter task index to delete: "))
            delete_task(task_index)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()
