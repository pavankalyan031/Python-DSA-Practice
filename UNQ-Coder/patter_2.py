"""
1
3
5
7
9

        * 
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
"""
n=5
for i in range(0,n):
    for j in range(i,n):
        print(' ', end=' ')
    for j in range(i):
        print("*", end=" ")
    for j in range(i+1):
        print("*", end=" ")
    print()
    
    
    
"""
9
7
5
3
1

* * * * * * * * *
  * * * * * * *
    * * * * *
     * * *
       *
"""

n=5
for i in range(0, n):
    for j in range(i+1):
        print(' ', end=" ")
    for j in range(i, n):
        print("*", end=" ")
    for j in range(i, n-1):
        print("*", end=" ")
    print()
    
    
    
    
n = 5
p = 1

# Upper Half
for i in range(n):

    # Spaces
    for j in range(i, n - 1):
        print(" ", end=" ")

    # Left Half
    for j in range(i):
        print(p, end=" ")

    # Right Half
    for j in range(i + 1):
        print(p, end=" ")

    p += 1
    print()
    
    
    
    n=5
p=1
for i in range (n-1):
    for j in range (i,n):
        print (' ', end = ' ')
    for j in range (i):
        print (p, end = ' ')   
    for j in range (i+1):
        print (p, end = ' ')   
    p+=1
    print()  
for i in range (n):
    for j in range (i+1):
        print (' ', end = ' ')
    for j in range (i,n-1):
        print (p, end = ' ')   
    for j in range (i,n):
        print (p, end = ' ')   
    p-=1
    print()
