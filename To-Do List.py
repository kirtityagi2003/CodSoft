class ToDoList:
    def __init__(self):
        self.tasks = []

    def display_tasks(self):
        if not self.tasks:
            print("Your to-do list is empty.")
        else:
            print("\n--- To-Do List ---")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")
            print("------------------")

    def add_task(self, new_task):
        self.tasks.append(new_task)
        print(f"\nTask '{new_task}' added to the to-do list.")

    def update_task(self, task_index, updated_task):
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1] = updated_task
            print(f"\nTask {task_index} updated to '{updated_task}'.")
        else:
            print("Invalid task index.")

    def remove_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            removed_task = self.tasks.pop(task_index - 1)
            print(f"\nTask {task_index} '{removed_task}' removed from the to-do list.")
        else:
            print("Invalid task index.")

    def clear_all_tasks(self):
        self.tasks = []
        print("\nAll tasks cleared from the to-do list.")

def main():
    todo_list = ToDoList()

    while True:
        print("\n--- To-Do List Application ---")
        print("1. Display tasks")
        print("2. Add task")
        print("3. Update task")
        print("4. Remove task")
        print("5. Clear all tasks")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            todo_list.display_tasks()
        elif choice == '2':
            new_task = input("Enter the new task: ")
            todo_list.add_task(new_task)
        elif choice == '3':
            task_index = int(input("Enter the task index to update: "))
            updated_task = input("Enter the updated task: ")
            todo_list.update_task(task_index, updated_task)
        elif choice == '4':
            task_index = int(input("Enter the task index to remove: "))
            todo_list.remove_task(task_index)
        elif choice == '5':
            todo_list.clear_all_tasks()
        elif choice == '6':
            print("Exiting the To-Do List Application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
