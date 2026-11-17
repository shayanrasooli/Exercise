# print(tasks)
def show_menu():
    while True:
        print("="*32)
        print("        TODO MANAGER")
        print("="*32)
        print("""
    1. Add New Task
    2. Show All Tasks
    3. CompleteTask
    4. Delete Task
    5. Show Statistics
    6. Exit
    """)

        choice= input("\nplease select as option: ")
        if choice.isdigit() and int(choice) in range (1,7):
            return choice
        else:
            print("Invalid Input. Try again!\n")

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
     


def add_task():
    task= input ("Enter task title: ")
    while True:
        print("""
        Available Priorities:
        Low
        Medium
        High
        """)
        priority= input ("Enter priority:\n")
        if priority in ("Low","Medium","High"):
            print ("Task added successfuly!")
            return {"title":task, "priority": priority}
        else:
            print ("invalid input!!")


def complete_task(tasks):
    task_id= int(input("Enter task ID: "))
    found= False
    for task in tasks:
        if task["id"]== task_id:
            found = True
            if task["done"]== True:
                print("Task is already completed!")
                return
            else:
                print("task has changed to complete!")
                task["done"] = True
                return

    if found == False:
        print("task is not found")
        return


def delet_task(tasks):
    task_id= int(input("Enter task ID you want to delet: "))
    found= False
    for task in tasks:
        if task["id"]== task_id:
            found=True
            tasks.remove(task)
            print("Task deleted successfully!")
            break
    
    if found == False:
        print("Task not found!")
        return
    for index, task in enumerate(tasks, start=1):
        task["id"]= index

def show_statistics(tasks):
    print("="*32)
    print("        Statistics")
    print("="*32)
    print(f"Total Tasks: {len(tasks)}")
    count=0
    high_tasks= 0
    medium_tasks= 0
    low_tasks= 0
    for task in tasks:
        if task["done"]== True:
            count += 1
        if task["priority"]== "High":
            high_tasks += 1
        if task["priority"]== "Medium":
            medium_tasks += 1
        if task["priority"]== "Low":
            low_tasks += 1

    print(f"Completed Tasks: {count}")
    print(f"Pending Tasks: {len(tasks) - count}")
    print("-"*20)
    print("Priority Statistic")
    print(f"High: {high_tasks}\nMedium: {medium_tasks}\nLow: {low_tasks}")



