"""def add(a,b): #a,b are parameters
    return a+b
    
print(add(10,20))"""


# triangle
def triangle():
    n=5
    for i in range(1, n+1):
        for j in range(1, i+1):
            print("*", end=" ")
        print()
        
triangle()