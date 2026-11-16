import json
import task_manager
import file_manager

with open("tasks.json", "r") as file:
    tasks = json.load(file)


while True:
    choice= task_manager.show_menu()
    print(choice)
    if choice == "1":
        new= task_manager.add_task()
        new["id"]= tasks[-1]["id"] + 1 if tasks else 1
        new["done"]= False
        tasks.append(new)
        
        with open("tasks.json","w") as file:
            json.dump(tasks, file, indent=4)
    
    elif choice == "2":
        file_manager.show_all_tasks(tasks)
    
    elif choice == "3":
        task_manager.complete_task(tasks)
        with open("tasks.json", "w") as file:
            json.dump(tasks, file, indent=4)

    elif choice == "6":
        break