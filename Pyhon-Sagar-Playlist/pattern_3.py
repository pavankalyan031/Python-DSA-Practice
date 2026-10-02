"""
print the pattern
* * * *
* * *
* * 
*

"""
n=4 # no.of rows
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()
