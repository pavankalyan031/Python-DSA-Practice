#using normal while method
"""list_1=[1,2,4,5,6,6,7,8]
left=0
right=len(list_1)-1
while left<right:
    list_1[left], list_1[right]= list_1[right], list_1[left]
    left+=1
    right-=1
    
print(list_1)"""


#using recursion
def reverse(arr, left, right):
    if left>=right:
        return
    
    arr[left], arr[right]=arr[right], arr[left] 
    reverse(arr, left+1, right-1)
    
arr=[1,2,3,4,5,6]
reverse(arr, 0, len(arr)-1)
print(arr)