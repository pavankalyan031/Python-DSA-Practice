"""
print patterns as
5
4 4
3 3 3
2 2 2 2
1 1 1 1 1
"""
n=5 
for i in range(n,0,-1):
    for j in range(n-i+1):
        print(i, end=" ")
    print()
    
    
"""
pattern
0
2 2 
4 4 4
6 6 6 6
8 8 8 8 8

"""
n=5
p=0
for i in range(1,n+1):
    for j in range(i):
        print(p, end=" ")
        
    p+=2
    print()

n=5
for i in range(1, n+1):
    for j in range(i):

        print(i+1, end=" ")
        
    print()    