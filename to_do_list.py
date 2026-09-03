tasks = []


def to_do_list():
    while True:
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Display Tasks")
        print("4. Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter Task: ")
            tasks.append(task)
        elif choice == '2':
            task = input("Enter the task you want to remove: ")
            if task in tasks:
                tasks.remove(task)
            else:
                print("Task not found!")
        elif choice == '3':
            if not tasks:
                print("No tasks yet.")
            else:
                print("Tasks:")
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task}")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid Choice")


if __name__ == "__main__":
    to_do_list()