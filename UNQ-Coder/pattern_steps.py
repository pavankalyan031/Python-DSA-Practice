"""
1. Outer Loop (for Rows / Number of Lines): 
The outer loop is strictly used to count the number 
of horizontal lines or rows in the pattern and handle moving down line-by-line.

2. Inner Loop (for Columns):
The inner loop focuses on handling the columns within each row. 
As a crucial trick, you need to connect the number
of iterations in the inner loop structurally to the current row number.

3. Always Print Inside the Inner Loop: 
Any actual character or symbol (like a star *) must always be printed
inside the inner loop, rather than the outer loop.

4. Symmetry Observation: 
This final step involves looking for symmetries or specific
geometric patterns. It is specifically utilized for 
solving more complex or advanced pattern questions (like diamonds).
"""

#example:
"""
8 8 8 8
8 8 8 8
8 8 8 8
8 8 8 8
"""
n=4 #optional since range is given in range(1,5) or range(0,4)
for i in range(1,n+1): #range(0,4)/range(1,5)
    for j in range(1, n+1):
        print('8', end=" ")
    print()
    
    
    
#patter-2
"""
*
**
***
****
*****
"""

n=5
for i in range(1,n+1): #range(0,n)
    for j in range(1,i+1): #range(0,i+1)
        print("*", end=" ")
    print()



"""
printing patterns
1
1 2
1 2 3 
1 2 3 4 
1 2 3 4 5
"""
n=5
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()
    
    
"""
printing patterns
1
2 2
3 3 3 
4 4 4 4 
5 5 5 5 5
"""
n=5
for i in range(1,n+1): #range(1,6)=> 1,2,3,4,5
    for j in range(1, i+1):
        print(i, end=" ")
    print()
    
    
    
"""
printing patterns
* * * * *
* * * *
* * *
* *
*
"""

n=5
#(5,0,-1)
#i=5,4,3,2,1
#first i=5
for i in range(n, 0, -1): 
    for j in range(i):
        print("*", end=" ")
    print()
    
    
#using while loop
n=5
i=n
while i>0: #5>0, 4>0, 3>0 ... 1>0 till run 
    print("* " *i)
    i-=1
    
    
"""
pattern print
1 2 3 4 5 6
1 2 3 4 5 
1 2 3 4 
1 2 3
1 2 
1
"""

n=6
# range(6,0,-1)
# ranges==> 6,5,4,3,2,1
#1st iteration: 6
for i in range(n, 0, -1):
    for j in range(1, i+1): #range(1,7)=> 1,2,3,4,5,6 in iteration 1
        #j has values like 1,2,3,4,5,6 so,print j 
        print(j, end=" ")
    print()
