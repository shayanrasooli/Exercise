def show_all_tasks(tasks):
    print("="*32)
    print("        TASK LIST")
    print("="*32)

    
    if not tasks:
        print("Task list is empty")
        return
    else:
        for task in tasks:
            print(f"ID: {task["id"]}")
            print(f"Title: {task["title"]}")
            print(f"Priority: {task["priority"]}")
            print(f"Status: {task["done"]}")
            print("-"*30)
        print(f"Total Task: {len(tasks)}")
     
