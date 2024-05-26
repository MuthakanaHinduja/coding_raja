Description: Develop a command-line to-do list application that allows users to manage tasks.

Features:

Task Management: Allow users to add, remove, and mark tasks as completed.
Task Priority: Implement a priority system for tasks (e.g., high, medium, low).
Due Dates: Enable users to set due dates for tasks.
List View: Display tasks in a list with their details.
Data Persistence: Store tasks in a file/database for persistence across sessions.
Tech Stack:

Python
File handling or a simple database library
code:
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

