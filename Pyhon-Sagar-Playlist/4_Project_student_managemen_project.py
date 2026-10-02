"""
dictionary:
collection of key:values


"""
"""
student={
    'Pavan': 100,
    'Shankar': 200,
    'Naveen': 300
}
print(student)

#accessing a element
print(student['Pavan'])


#update the element
student['Naveen']= 500
print(student)


#delete
del student['Shankar']
print(student)"""



#student managament system :
"""
1. add
2. update
3. del
4. view
"""

student={}

def add_student(name, grade):
    student[name]=grade #[Pavan]=100
    print(f"{name} is added with {grade}") #Pavan is added with 100
    
    
    
def update_student(name, grade):
    if name in student:
        student[name]=grade
        print(f"{name} updated with the {grade}")
    else:
        print(f"{name} is not found")
        
        
def delete_student(name):
    if name in student:
        del student[name]
        print(f"{name} is deleted")
    else:
        print(f"{name} is not found")
        
        
        
def display_all_student():
    if student:
        for name, grade in student.items():
            print(f"{name} : {grade}")
            
    else:
        print("No student is found")
        
     



def main():
    while True: 
        print("\n Student Management System")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. Display Student")
        print("5. Exit")
        
        
        user_choice= input("Enter a choice to start.. : ")
        
        if user_choice=="1":
            name=input("Enter the name: ")
            grade= int(input("Enter the grade to add: "))
            add_student(name, grade)
            
        elif user_choice=="2":
            name= input("Enter the name: ")
            grade= int(input("Enter the updated grade: "))
            update_student(name, grade)
            
        elif user_choice=="3":
            name= input("Enter the name to delete: ")
            delete_student(name)
            
            
        elif user_choice=="4":
            display_all_student()
            
        
        elif user_choice=="5":
            print("Thank you!")
            break
        
        else:
            print("Invalid input!!!")
        

main()