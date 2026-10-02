"""
Pattern 6
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
"""
n=5
for i in range(1, n+1):
    
    #space in decrease order n-i
    for j in range(n-i):
        print(" ", end=" ")
        
        #row increase order like 1, 3, 5, 7, 9 odrer means 2*i-1
        # lets i=1 
    for j in range(2*i-1):
            print("*", end=" ")
            
    print()