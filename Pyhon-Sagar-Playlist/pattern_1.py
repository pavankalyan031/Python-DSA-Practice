"""
1. print the pattern
*****
*****
*****
*****
*****

"""
n=int(input("Enter the no. of lines: ")) # no. of rows 
for i in range(1,n+1): # rows
    for j in range(1,n+1): # columns
        print("*", end=" ")
    print()
    
"""
n=5
for i in range(1,5+1) ==> i= 1,2,3,4,5
step 1: i=1 # outer loop

for j in range(1,5+1) ==> j=1,2,3,4,5

step 2: now i=1 and enters into inner loop j=1 ==> * and then j=2 ==> ** similarlly 
j=1,2,3,4,5 ==> ***** now ends=" "==> * * * * *
the print() ==> new line 

step 3: now i=2 
same happens

finally:
i=1 ==< j=1,2,3,4,5 ==> * * * * *

"""

    
    