"""Optimal solution"""

#check an array is sorted or not?
#True or False
"""nums=[1,2,4,5,3,6,10]
n=len(nums)
nums.sort()
for i in range(0,n):
    if nums.sort():
        print(True)
    else:
        print(False)"""
        
        
def check_sorted(nums):
    n=len(nums)
    for i in range(0, n-1): #since i and i+1 is there so, i must be go for n-1 then it excluded
        if nums[i]>nums[i+1]:
            return False
        
    return True

nums=[1,2,3,4,5,13,19,20]
print(check_sorted(nums))