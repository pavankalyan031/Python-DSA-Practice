# Problem 1: Reverse a List
# Problem Statement

# Given a list of elements, return a new list with all elements in reverse order.

# Example:

# Input:
# [1, 2, 3, 4]

# Output:
# [4, 3, 2, 1]

#using function 
def reverse_list(a):
    b=[] #to store reverse list
    for i in range(len(a)-1, -1, -1):
        b.append(a[i])
    return b

print(reverse_list([1,2,3,4]))


# using 2 pointers --> ** best for interview
def reverse_list(num):
    left=0
    right=len(num)-1
    
    while left<right:#true 1<2 and false 2<1
        num[left], num[right]= num[right], num[left]
        left+=1
        right-=1
        
    return num
num=[1,2,3,4]
result=reverse_list(num)
print(result)
        



#approach -1 - slicing
n=[1,2,3,4]
# reverse=n[::-1] 
# print(reverse)
print(n[::-1])



# approach 2 - reverse() function
#reverse() method reverses the elements of the list in-place and it modifies the original list without creating a new list.
n=[1,2,3,4]
n.reverse()
print(n)



# using approach of reversed() function
#Python's built-in reversed() function is another way to reverse the list. However, reversed() returns an iterator, so it needs to be converted back into a list.
n=[1,2,3]
rev= list(reversed(n))
print(rev)


#using insert() function 
n=[1,2,3]
list_1=[]
for i in n:
    list_1.insert(0,i)
    
print(list_1)




#using function
