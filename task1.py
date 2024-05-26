import json
import os
from datetime import datetime

# File to store tasks
TASK_FILE = "tasks.json"

# Function to load tasks from file
def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as file:
            return json.load(file)
    else:
        return {"tasks": []}

# Function to save tasks to file
def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Function to add a task
def add_task(tasks):
    task_name = input("Enter task name: ")
    priority = input("Enter priority (high/medium/low): ")
    due_date_str = input("Enter due date (YYYY-MM-DD): ")
    try:
        due_date = datetime.strptime(due_date_str, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return

    tasks["tasks"].append({
        "name": task_name,
        "priority": priority,
        "due_date": due_date_str,
        "completed": False
    })
    save_tasks(tasks)
    print("Task added successfully.")

# Function to remove a task
def remove_task(tasks):
    print("Select task to remove:")
    for idx, task in enumerate(tasks["tasks"]):
        print(f"{idx + 1}. {task['name']} - Priority: {task['priority']} - Due Date: {task['due_date']}")
    choice = input("Enter task number to remove: ")
    try:
        choice = int(choice)
        if 1 <= choice <= len(tasks["tasks"]):
            del tasks["tasks"][choice - 1]
            save_tasks(tasks)
            print("Task removed successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Function to mark a task as completed
def mark_completed(tasks):
    print("Select task to mark as completed:")
    for idx, task in enumerate(tasks["tasks"]):
        print(f"{idx + 1}. {task['name']} - Priority: {task['priority']} - Due Date: {task['due_date']}")
    choice = input("Enter task number to mark as completed: ")
    try:
        choice = int(choice)
        if 1 <= choice <= len(tasks["tasks"]):
            tasks["tasks"][choice - 1]["completed"] = True
            save_tasks(tasks)
            print("Task marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Function to display all tasks
def display_tasks(tasks):
    if not tasks["tasks"]:
        print("No tasks.")
    else:
        print("Tasks:")
        for idx, task in enumerate(tasks["tasks"]):
            status = "Completed" if task["completed"] else "Not Completed"
            print(f"{idx + 1}. {task['name']} - Priority: {task['priority']} - Due Date: {task['due_date']} - Status: {status}")

# Main function
def main():
    tasks = load_tasks()
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. Display Tasks")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            remove_task(tasks)
        elif choice == "3":
            mark_completed(tasks)
        elif choice == "4":
            display_tasks(tasks)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
