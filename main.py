import os

def main():
    check_file_existence()
    separate()
    print("Ready to do some tasks!")
    open_list()
    separate()
    while True:
        print("What do you want to do:")
        print("1. Edit       2. Exit")
        usr_choice = str(input("->").lower())
        separate()
        if usr_choice in ("edit","1"):
            print("You wanna: 1. Add  2.Remove")
            edit_choice = str(input("->")).lower()
            separate()
            if edit_choice in ("add","1"):
                print("Enter the new task:")
                task_to_add = input("->")
                add_task(task_to_add)
                open_list()
                separate()
            elif edit_choice in ("remove","2"):
                print("Enter the no. of task to be removed:")
                task_to_remove = int(input("->"))
                remove_task(task_to_remove)
                open_list()
                separate()
            else:
                pass
        elif usr_choice in ("exit","2"):
            return False
        else:
            pass
        
    
def open_list():
    with open("tasks.txt", "rt") as file:
        contents= file.readlines()
        tasks = [content.strip().capitalize() for content in contents]
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")
            
            
def add_task(new_task):
    with open("tasks.txt","a") as file:
        file.write(new_task + "\n")
        
        
def remove_task(old_task_no):
    lines = []
    with open("tasks.txt","r") as file:
            lines = file.readlines()
            
    with open("tasks.txt", "w") as file:
            for i, line in enumerate(lines):
                    if i != (old_task_no - 1):
                            file.write(line)
                            
                            
def check_file_existence():
    if  not os.path.exists("tasks.txt"):
        with open("tasks.txt","x"):
            pass    
                
            
def separate():
    separator = "================================="
    print(separator)
        

main()