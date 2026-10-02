# my_list=["hello", 1010, 20, "M"]
# print(my_list)


# list_1=[1,2,3,4]
# print(list_1[1:3:2])




"""
def a function 
5 inputs from user 
ex: num 1= 10
....

sum= of the numbers
"""

def sum():
    lst=[]
    user= int(input("Enter the no.of inputs: "))
    for i in range(user):
        user= int(input(f"Enter element {i}: "))
        lst.append(user)
    print(lst)
        
    total=0
    for i in range(len(lst)):
        total=total+lst[i]
        
    
    
    
    
    return f"total is = {total}"

a= sum()
print(a)