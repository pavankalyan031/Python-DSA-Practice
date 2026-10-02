#find the pair which have the difference of 
#eg: 1,5,4,3,2 here 1,3 and 2,4 and 5,3 are have difference of 2 means when sub we get 2
#k=2

#interview based approach
def find_pair(n, k):
    for i in n:
        if i+k in n:
            print((f"Values are: ({i}, {i+k})"))
            # print((i, i+k))
                 
n={1,2,4,5,3}
k=2
find_pair(n,k)