# Simple To-Do List Program

tasks = []  # empty list to store tasks

while True:
    print("\n--- To-Do List Menu ---")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        task = input("Enter a new task: ")
        tasks.append(task)
        print("✅ Task added!")

    elif choice == "2":
        print("\nYour Tasks:")
        if not tasks:
            print("No tasks yet!")
        else:
            for i, t in enumerate(tasks, start=1):
                print(f"{i}. {t}")

    elif choice == "3":
        print("\nWhich task do you want to remove?")
        for i, t in enumerate(tasks, start=1):
            print(f"{i}. {t}")
        try:
            task_num = int(input("Enter task number: "))
            removed = tasks.pop(task_num - 1)
            print(f"🗑️ Removed: {removed}")
        except (ValueError, IndexError):
            print("Invalid choice!")

    elif choice == "4":
        print("👋 Goodbye! Your to-do list is closed.")
        break

    else:
        print("Invalid option, please try again.")
