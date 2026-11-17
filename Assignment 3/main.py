import json
import task_manager
import file_manager

tasks= file_manager.read_file()

while True:
    choice= task_manager.show_menu()
    print(choice)
    if choice == "1":
        new= task_manager.add_task()
        new["id"]= tasks[-1]["id"] + 1 if tasks else 1
        new["done"]= False
        tasks.append(new)
        
        file_manager.rewrite(tasks)
    
    elif choice == "2":
        task_manager.show_all_tasks(tasks)
    
    elif choice == "3":
        task_manager.complete_task(tasks)
        file_manager.rewrite(tasks)

    elif choice == "4":
        task_manager.delet_task(tasks)
        file_manager.rewrite(tasks)

    elif choice == "5":
        task_manager.show_statistics(tasks)

    elif choice == "6":
        print("Goodbye!")
        print("See you next time.")
        break