"""using brute force approach
worst case tc= O(2n) similar to O(n)
worst case sc = O(n) dict using to store upto n unique keys"""
def remove_duplicate(nums):
    n=len(nums)
    freq_map={} #empty dictionary since it allow unique elements and maintain order
    for i in range(0,n):
        freq_map[nums[i]]=0
    
    j=0
    for k in freq_map:
        nums[j]=k
        j+=1
        
    return j

nums=[1,2,3,3,4,5,5,6,7,8,9,9,10]
print(remove_duplicate(nums))
        
        
"""using optimal solution
tc= O(n)
sc= O(1)"""

def remove_duplicate(nums):
    n=len(nums)
    if n==1:
        return 1
    i=0
    j=i+1
    while j<n:
        if nums[j]!=nums[i]:
            i+=1
            nums[i], nums[j]= nums[j], nums[i]
            
        j+=1
    
    return i+1

nums=[1,2,3,4,4,5,6,7,7,8,9,10]
print(remove_duplicate(nums))