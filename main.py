def main():
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
            if edit_choice == "add" or "1":
                print("Add")
                separate()
            else:
                print("Remove")
                separate()
        elif usr_choice in ("exit","2"):
            return False
        
    
def open_list():
    with open("tasks.txt", "r") as file:
        contents= file.readlines()
        tasks = [content.strip().capitalize() for content in contents]
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")
            
            
def separate():
    separator = "================================="
    print(separator)
        

main()