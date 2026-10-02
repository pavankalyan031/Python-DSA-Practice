"""
find max and min and take input from user
lst=[1,3,3,4,4]
max
min
"""

def max_min():
    lst=[]
    user=int(input("Enter no.of elements: "))
    for i in range(user):
        num=int(input("Enter the element {i}: "))
        lst.append(num)
    print(lst)
    maximum=max(lst)
    minimum=min(lst)
    
    return f"Maximum is {maximum} & Minimum is {minimum}"

b=max_min()
print(b)