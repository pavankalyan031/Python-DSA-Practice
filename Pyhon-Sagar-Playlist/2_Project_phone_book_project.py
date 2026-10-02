#phone book mini project
"""fearures:
1. able to add new contacts= name+phone by user to add new contact in the phone book

2. search by name and display number

3. delete by name to contact

4. display all contact book

5. exit: terminate the application

"""

"""#empty dict
Phone_Book={}
while True:
    
    print("<===Phone Book===>")
    print("1. Add a Contact")
    print("2. Search a Contact")
    print("3. Delete a Contact")
    print("4. Display all Contacts")
    print("5. Exit()")
    
    user= input("Enter your Choice: ")
    
    #Add contact:
    if user=="1":
        name= input("Enter the name: ")
        number=int(input("Enter the number: "))
        
        if name in Phone_Book:
            print("Contact is already exist!")
            
        else:
            Phone_Book[name]=number
            print("Contact is added successfully😊")
            
 
        
    #Search contact
    elif user=="2":
        name=input("Enter the name to search: ")
        
        if name in Phone_Book:
            print(f"{name} : {Phone_Book[name]}")
            
        else:
            print("Contact is not found!")
            
            
    # Delete the contact
    elif user=="3":
        
        name= input("Enter the name to delete the contact: ")
        
        if name in Phone_Book:
            del Phone_Book[name]
            print("Deleted Successfully")
            
        else:
            print("Contact is not found!")
            
            
    #Display all contacts
    elif user=="4":
        
        if Phone_Book:
            
            print("\nContacts")
            
            for name, number in Phone_Book.items():
                print(f"{name:<15} : {number}")
                
        else:
            print("Phone Book is empty!")
            
            
            
    #Exit
    elif user=="5":
        
        print("Thank you😊")
        break
    
    else:
        print("Invalid input")


"""

"""
Phone_Book={
    'Pradeep': 123,
    'Manisha': 456,
    "Charandas": 789,
    "Pushpa": 123,
    "Pavan": 456
    
}

print("List of Contact: \nPradeep: 123\nManisha: 456\nCharandas: 789\nPusha: 123\nPavan: 456")

#add new contact"""





def add_contact(phonebook):
    name= input("Enter contact name: ").strip().title()
    
    if name in phonebook:
        print(f"{name} already exist!")
        return 
    
    number=input("Enter phone number: ").strip()
    
    if not number.isdigit():
        print("Invalid number!")
        return
    
    phonebook[name]=number
    print(f"{name} is added successfully")
    
    
def search_contact(phonebook):
    
    name= input("Enter contact name: ").strip().title()
    
    if name in phonebook:
        print(f"{name} : {phonebook[name]}")
    else:
        print("Not found")
    
    
def update_contact(phonebook):
    
    name=input("Enter contact name: ").strip().title()
    
    if name not in phonebook:
        print("Contact not found")
        return
    
    new_num=input("Enter new number: ").strip()
    
    if not new_num.isdigit():
        print("Invalid number!")
        return
    
    
    phonebook[name]=new_num
    print("Contact updated")
    
    
    
def del_contact(phonebook):
    
    name= input("Enter contact name: ").strip().title()
    
    if name in phonebook:
        del phonebook[name]
        print("Deleted successfully")
    else:
        print("Contact is not found")
        
        
def display_contact(phonebook):
    
    if not phonebook:
        print("Phonebook is empty")
        return
    
    print("\n=== Contact List ===")
    
    for name, num in phonebook.items():
        print(f"{name:<15} : {num}")
        
        
        


def menu():
    
    print("\n==== Phone Book ====")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Display All Contacts")
    print("6. Exit")
    
    
phonebook={}

while True:
    
    menu()
    
    choice=input("Enter your choice: ")
    
    if choice=="1":
        add_contact(phonebook)
        
    elif choice=="2":
        search_contact(phonebook)
    
    elif choice=="3":
        update_contact(phonebook)
        
    elif choice=="4":
        del_contact(phonebook)
        
    elif choice=="5":
        display_contact(phonebook)
        
    elif choice=="6":
        print("Thank you")
        break
    
    else:
        print("Invalid Input")