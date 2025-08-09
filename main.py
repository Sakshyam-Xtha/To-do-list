def main():
    print("Ready to do some tasks!")
    open_list()
    
    
def open_list():
    with open("tasks.txt", "r") as file:
        contents= file.readlines()
        tasks = [content.strip().capitalize() for content in contents]
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")
        
        
main()