def main():
    print("Ready to do some tasks!")
    open_list()
    
    
def open_list():
    with open("tasks.txt", "r") as file:
        content = file.readlines()
        print(content[i] for i in range (len(content)))
        
        
main()