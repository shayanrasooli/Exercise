import json

def read_file():
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks= []
    return tasks

def rewrite(tasks):
    with open("tasks.json","w") as file:
            json.dump(tasks, file, indent=4)