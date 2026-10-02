#for loop
"""
start, stop, step
for i in range(start, stop, step):
 statements
 
 include -
 exclude - 
"""


"""#print 1-10
n=int(input())
for a in range(1,n+1):
    print(a)
    """
    
"""#print even number
n=int(input("Enter a num: "))
for i in range(2, n+1, 2):
    print(i)"""
    
n=int(input("Start Num: "))
m=int(input("End Num: "))

a= int(input("Enter number to divisible: "))

for i in range(n, m+1):
    
    if i%a==0:
        print(i)


