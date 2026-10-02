"""
5. pattern print
54321
4321
321
21
1

"""
n=5
for i in range(n, 0, -1): #i= 5 4 3 2 1
    # first iteration i=5
    for j in range(i, 0, -1):
    # we have to print 5 4 3 2 1 means goes from i then 0 -1
      print(j, end=" ")
    print()