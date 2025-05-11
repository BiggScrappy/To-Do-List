# Simple To-Do List Program in Python

class TodoList:
    def __init__(self):
        self.tasks = []

    def show_tasks(self):
        if not self.tasks:
            print("Your to-do list is empty.")
        else:
            print("\nYour To-Do List:")
            for idx, task in enumerate(self.tasks, start=1):
                print(f"{idx}. {task}")
    
    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added successfully!")

    def remove_task(self, task_number):
        try:
            task_number = int(task_number) - 1
            if 0 <= task_number < len(self.tasks):
                removed_task = self.tasks.pop(task_number)
                print(f"Task '{removed_task}' removed successfully!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    todo_list = TodoList()
    
    while True:
        print("\nOptions:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")
        
        choice = input("Select an option (1/2/3/4): ")
        
        if choice == '1':
            todo_list.show_tasks()
        elif choice == '2':
            task = input("Enter the task you want to add: ")
            todo_list.add_task(task)
        elif choice == '3':
            todo_list.show_tasks()
            task_number = input("Enter the number of the task you want to remove: ")
            todo_list.remove_task(task_number)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
