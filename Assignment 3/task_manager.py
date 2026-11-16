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
    

