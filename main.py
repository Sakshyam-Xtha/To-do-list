import os

def main():
    check_file_existence()
    separate()
    print("Ready to do some tasks!")
    open_list()
    separate()
    while True:
        edit_choice = menu()
        if edit_choice != False:
            separate()
            if edit_choice in ("add task","1"):
                print("Enter the new task:")
                task_to_add = input("->")
                add_task(task_to_add)
                separate()
                open_list()
                separate()
            elif edit_choice in ("remove task","2"):
                open_list()
                task_to_remove = take_inp_num("Enter the no. of task to be removed:")
                separate()
                remove_task(task_to_remove)
                open_list()
                separate()
            elif edit_choice in ("mark done", "3"):
                open_list()
                completed_task_num = take_inp_num("What task do you wanna mark done:")
                if check_marked(completed_task_num):
                    remove_mark(completed_task_num - 1)
                mark_done(completed_task_num - 1)
                separate()
                open_list()
                separate()
            elif edit_choice in ("mark important", "4"):
                open_list()
                important_task_num = take_inp_num("What task do you wanna mark important:")
                if check_marked(important_task_num):
                    remove_mark(important_task_num - 1)
                mark_important(important_task_num - 1)
                separate()
                open_list()
                separate()
            elif edit_choice in ("remove mark", "5"):
                open_list()
                marked_task_num = take_inp_num("What task do you wanna remove mark from:")
                remove_mark(marked_task_num - 1)
                separate()
                open_list()
                separate()
            else:
                pass
        else:
            break

    
def open_list():
    if os.path.getsize("tasks.txt") != 0:
        print("-----------YOUR-LIST-------------")
        with open("tasks.txt", "rt") as file:
            contents= file.readlines()
            tasks = [content.strip().capitalize() for content in contents]
            for i, task in enumerate(tasks):
                print(f"{i+1}. {task}")
    else:
        print("-----------YOUR-LIST-------------")
        print("No tasks added.")
                
            
def add_task(new_task):
    with open("tasks.txt","a") as file:
        file.write(new_task + "\n")
        
        
def remove_task(old_task_no):
    lines = read_file()
            
    with open("tasks.txt", "w") as file:
            for i, line in enumerate(lines):
                    if i != (old_task_no - 1):
                            file.write(line)
                            
                            
def check_file_existence():
    if  not os.path.exists("tasks.txt"):
        with open("tasks.txt","x"):
            pass    
        
        
def mark_done(completed_task):
    lines = read_file()
            
    with open("tasks.txt","w") as file:
            for i, line in enumerate(lines):
                    if i in [completed_task]:
                        file.write(line.rstrip("\n") + "\t{✓}" + "\n") 
                    else:
                            file.write(line)
         
         
def mark_important(important_task):
    lines = read_file()
        
    with open("tasks.txt", "w") as file:
        for i, line in enumerate(lines):
            if i in [important_task]:
                file.write(line.rstrip("\n") + "\t{*}" + "\n")
            else:
                file.write(line)
                            
             
def remove_mark(marked_task):
    lines = read_file()
        
    with open("tasks.txt", "w") as file:
        for i, line in enumerate(lines):
            if i == marked_task:
                file.write(line.replace("\t{*}", "").replace("\t{✓}", ""))
            else:
                file.write(line)
    
    
def check_marked(task_num):
    lines = read_file()
    line = lines[task_num-1]
    if "\t{*}" in line or "\t{✓}" in line:
        return True
    else:
        return False
    
def read_file():
    lines = []
    with open("tasks.txt", "r") as file:
        lines = file.readlines()
    return lines
             
                            
def get_file_length():
    return len(read_file())
                    
            
def separate():
    separator = "================================="
    print(separator)
    
    
def take_inp_num(prompt):
    while True:
        try:
            print(prompt)
            usr_inp = int(input("->"))
            if usr_inp <= 0 and usr_inp > get_file_length():
                raise ValueError
            return usr_inp
        except ValueError:
            separate()
            print("Enter the correct task number.")
            separate()
    
    
def menu():
    print("What do you want to do:")
    print("1. Edit       2. Exit")
    try:
        usr_choice = str(input("->").lower())
        separate()
        if usr_choice in ("edit","1"):
            print("You wanna: \n1. Add task  2. Remove task \n3. Mark  done  4. Mark important\n5. Remove mark")
            operation = str(input("->")).lower()
            if operation in ("1","2","3","4","5","add task", "remove task","mark done","mark important","remove mark"):
                return operation
            else:
                raise ValueError
        elif usr_choice in ("exit","2"):
            return False
        else:
            pass
    except ValueError:
        separate()
        print("Enter a valid input.") 
        separate()  
    
    
main()