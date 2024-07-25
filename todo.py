import json

# Function to load tasks from a file
def load_tasks(filename):
    try:
        with open(filename, 'r') as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []
    return tasks

# Function to save tasks to a file
def save_tasks(tasks, filename):
    with open(filename, 'w') as file:
        json.dump(tasks, file, indent=4)

# Function to display the menu
def display_menu():
    print("To-Do List Application")
    print("----------------------")
    print("1. Add a new task")
    print("2. View all tasks")
    print("3. Mark a task as completed")
    print("4. Delete a task")
    print("5. Save tasks")
    print("6. Load tasks")
    print("7. Exit")

# Function to add a new task
def add_task(tasks):
    task = input("Enter the new task: ")
    tasks.append({"task": task, "completed": False})
    print("Task added!")

# Function to view all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasks):
            status = "Completed" if task["completed"] else "Not completed"
            print(f"{i + 1}. {task['task']} [{status}]")

# Function to mark a task as completed
def mark_task_completed(tasks):
    view_tasks(tasks)
    task_number = int(input("Enter the task number to mark as completed: "))
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]["completed"] = True
        print("Task marked as completed!")
    else:
        print("Invalid task number.")

# Function to delete a task
def delete_task(tasks):
    view_tasks(tasks)
    task_number = int(input("Enter the task number to delete: "))
    if 0 < task_number <= len(tasks):
        tasks.pop(task_number - 1)
        print("Task deleted!")
    else:
        print("Invalid task number.")

def main():
    tasks = []
    filename = "tasks.json"

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_task_completed(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            save_tasks(tasks, filename)
            print("Tasks saved to file.")
        elif choice == '6':
            tasks = load_tasks(filename)
            print("Tasks loaded from file.")
        elif choice == '7':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()