todo = {}  # Global dictionary to store tasks

def add_todo():
    # Start key_counter from the next available key
    key_counter = len(todo) + 1  
    while True:
        value = input("Enter the new task (or type 'exit' to stop): ")
        if value.lower() == 'exit':
            break
        
        todo[key_counter] = value
        key_counter += 1
        
    print("\nTask(s) added successfully!")

def delete_todo():
    if not todo:
        print("\nYour todo list is empty. Nothing to delete.")
        return

    try:
        key = int(input("\nEnter the task number to delete: "))
        if key in todo:
            del todo[key]
            print(f"Task {key} deleted successfully!")
        else:
            print(f"Task {key} not found!")
    except ValueError:
        print("Invalid input! Please enter a valid task number.")

def display_todo():
    if not todo:
        print("\nYour todo list is empty.")
    else:
        print("\nYour Todo List:")
        for key, value in todo.items():
            print(f"{key}: {value}")

def main():
    while True:
        print("\nTodo List Menu:")
        print("1. Add a new task")
        print("2. Delete a task")
        print("3. Display all tasks")
        print("4. Exit")
        
        try:
            option = int(input("Enter your option (1-4): "))
            match option:
                case 1:
                    add_todo()
                case 2:
                    delete_todo()
                case 3:
                    display_todo()
                case 4:
                    print("Exiting... Goodbye!")
                    break
                case _:
                    print("Invalid option! Please select a valid option (1-4).")
        except ValueError:
            print("Invalid input! Please enter a number (1-4).")

# Run the program
main()
