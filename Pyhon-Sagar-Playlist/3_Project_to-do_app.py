def task():
    tasks=[]
    total_task=int(input("enter no. of tasks want to add: "))
    for i in range(1, total_task+1):
        task_name= input("Enter task name : ")
        tasks.append(task_name)
        
        
    print(f"Today tasks are:\n{tasks}")
    
    while True:
        choice= input("Enter operation to perform\n1-Add\n2-Search\n3-Update\n4.Delete\n5.Display\n6-Exit\nEnter your choice in numbers: ...")
        
        if choice=="1":
            add=input("Enter task name: ")
            tasks.append(add)
            print(f"Task is added successfully: {add}")
            
            
        elif choice =="2":
            task_name=input("Enter name of the task to search: ")
            if task_name in tasks:
                print(f"{task_name} is available in the list {tasks}")
            else:
                print(f"{task_name} is not available")
        
        
        elif choice == "3":
            updated_value=input("enter task name to update: ")
            if updated_value in tasks:
                new_task= input("enter new task: ")
                ind= tasks.index(updated_value)
                tasks[ind]= new_task
                print(f"updated task {new_task}")
                
                
        elif choice=="4":
            del_value= input("enter name of the task to delete: ")
            if del_value in tasks:
                ind= tasks.index(del_value)
                del tasks[ind]
                print(f"Task {del_value} is deleted...")
            else:
                print(f"Task {del_value} is not available")
                
                
        elif choice == "5":
                print(f"Total tasks are {tasks}")
                
                
        elif choice == "6":
            print("Thank you!")
            break
                
        
        else:
            print("Invalid input!")   
        
task()
