"""
Pattern 7 (Diamond)
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
"""
# diamond as -
# upper pyramid and 
# lower pyramid


n= 5 # lets we are doing for upper means till row 5
for i in range(1, n+1):
    
    #space n-1 decrease
    for j in range(n-i):
        print(" ", end=" ")
    
    #for rows as increase by 1, 3, 5, 7 means 2*-i-1 lets
    # i=1 -> 2-1-1= 0 means like 0 starts --> range()
    for j in range(2*i-1):
        print("*", end=" ")
    print()
    
# lower pyramid
for i in range(n-1, 0, -1):
    for j in range(n-i):
        print(" ", end=" ")
    for j in range(2*i-1):
        print("*", end=" ")
    print()
    