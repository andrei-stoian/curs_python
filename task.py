import json
import os


TASKS_FILE = "tasks.json"
CATEGORIES_FILE = "categories.json"


tasks = {}
categories = {}


def load_data():
    global tasks, categories
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as tasks_file:
            tasks = json.load(tasks_file)
    if os.path.exists(CATEGORIES_FILE):
        with open(CATEGORIES_FILE, "r") as categories_file:
            categories = json.load(categories_file)


def save_data():
    with open(TASKS_FILE, "w") as tasks_file:
        json.dump(tasks, tasks_file, indent=4)
    with open(CATEGORIES_FILE, "w") as categories_file:
        json.dump(categories, categories_file, indent=4)


def add_category():
    while True:
        category_name = input("Enter the category name: ")
        if category_name not in categories:
            categories[category_name] = True
            print(f"Category '{category_name}' added successfully.")
            break
        else:
            print("Error: Category already exists.")


def add_task():
    task_name = input("Enter the task name: ")
    due_date = input("Enter the due date (e.g., 22.01.2022 21:30): ")
    responsible_person = input("Enter the responsible person: ")
    category = input("Enter the category: ")

    if category not in categories:
        print("Error: Category does not exist.")
    elif task_name in tasks:
        print("Error: Task already exists.")
    else:
        tasks[task_name] = {
            "due_date": due_date,
            "responsible_person": responsible_person,
            "category": category,
        }
        print("Task added successfully.")


def list_tasks():
    print("\n--- Tasks ---")
    for task_name, task_details in tasks.items():
        print(f"Task: {task_name}")
        print(f"Due Date: {task_details['due_date']}")
        print(f"Responsible Person: {task_details['responsible_person']}")
        print(f"Category: {task_details['category']}")
        print("-" * 30)


def list_sorted_tasks(sort_key, reverse=False):
    sorted_tasks = sorted(tasks.items(), key=lambda x: x[1][sort_key], reverse=reverse)
    print("\n--- Tasks Sorted by", sort_key.capitalize(), "---")
    for task_name, task_details in sorted_tasks:
        print(f"Task: {task_name}")
        print(f"Due Date: {task_details['due_date']}")
        print(f"Responsible Person: {task_details['responsible_person']}")
        print(f"Category: {task_details['category']}")
        print("-" * 30)


def filter_tasks(filter_key):
    filter_string = input(f"Enter a string to filter {filter_key}: ").lower()
    filtered_tasks = {
        task_name: task_details for task_name, task_details in tasks.items()
        if filter_string in task_details[filter_key].lower()
    }
    print("\n--- Filtered Tasks by", filter_key.capitalize(), "---")
    for task_name, task_details in filtered_tasks.items():
        print(f"Task: {task_name}")
        print(f"Due Date: {task_details['due_date']}")
        print(f"Responsible Person: {task_details['responsible_person']}")
        print(f"Category: {task_details['category']}")
        print("-" * 30)


def edit_task(task_name):
    if task_name not in tasks:
        print("Error: Task does not exist.")
        return

    task_details = tasks[task_name]
    print(f"Editing Task: {task_name}")
    print(f"Current Due Date: {task_details['due_date']}")
    new_due_date = input("Enter the new due date (or press Enter to keep current): ").strip()
    if new_due_date:
        task_details['due_date'] = new_due_date

    print(f"Current Responsible Person: {task_details['responsible_person']}")
    new_responsible_person = input("Enter the new responsible person (or press Enter to keep current): ").strip()
    if new_responsible_person:
        task_details['responsible_person'] = new_responsible_person

    print(f"Current Category: {task_details['category']}")
    new_category = input("Enter the new category (or press Enter to keep current): ").strip()
    if new_category:
        if new_category in categories:
            task_details['category'] = new_category
        else:
            print("Error: New category does not exist.")

    print("Task edited successfully.")


def delete_task(task_name):
    if task_name not in tasks:
        print("Error: Task does not exist.")
        return

    del tasks[task_name]
    print("Task deleted successfully.")


# Main menu
def main():
    load_data()

    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Add Category")
        print("2. Add Task")
        print("3. List Tasks")
        print("4. List Tasks Sorted")
        print("5. Filter Tasks")
        print("6. Edit Task")
        print("7. Delete Task")
        print("8. Save and Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_category()
        elif choice == "2":
            add_task()
        elif choice == "3":
            list_tasks()
        elif choice == "4":
            print("\n--- Sort Options ---")
            print("1. Sort by Task")
            print("2. Sort by Due Date")
            print("3. Sort by Responsible Person")
            print("4. Sort by Category")
            sort_option = input("Enter sort option: ")
            reverse = False
            if sort_option not in ["1", "2", "3", "4"]:
                print("Invalid sort option.")
                continue
            if sort_option in ["2", "3"]:
                reverse = input("Sort in reverse (y/n)? ").strip().lower() == "y"
            list_sorted_tasks("task" if sort_option == "1" else "due_date" if sort_option == "2" else
            "responsible_person" if sort_option == "3" else "category", reverse)
        elif choice == "5":
            print("\n--- Filter Options ---")
            print("1. Filter by Task")
            print("2. Filter by Due Date")
            print("3. Filter by Responsible Person")
            print("4. Filter by Category")
            filter_option = input("Enter filter option: ")
            if filter_option not in ["1", "2", "3", "4"]:
                print("Invalid filter option.")
                continue
            filter_tasks("task" if filter_option == "1" else "due_date" if filter_option == "2" else
            "responsible_person" if filter_option == "3" else "category")
        elif choice == "6":
            task_to_edit = input("Enter the name of the task to edit: ")
            edit_task(task_to_edit)
        elif choice == "7":
            task_to_delete = input("Enter the name of the task to delete: ")
            delete_task(task_to_delete)
        elif choice == "8":
            save_data()
            print("Data saved successfully. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()