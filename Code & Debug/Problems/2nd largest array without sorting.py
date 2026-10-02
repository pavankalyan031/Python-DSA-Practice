"""Brute force approach
Time = O(nlogn) ==> sorting time complexity 
Space= O(1)"""
nums= [1,2,3,5,6,0,5]
# n=len(nums)
nums.sort()
print(nums[-2])
# print(nums[n-2])




"""Best solution
Tc= O(n)+O(n)=O(2n) ==> Similar to O(n) since 2 is constant
space c= O(1) using only fixed number of variables
"""
nums= [10,203,40,60,-20,0,33]
n=len(nums)
largest=float("-inf")
second_largest=float("-inf")

for i in range(0,n):
    largest=max(largest, nums[i])
    
for i in range(0,n):
    if nums[i]>second_largest and nums[i]!= largest:
        second_largest= nums[i]
    
    
     
print(second_largest)  

 
"""Optimal Solution
Tc= O(n) using only 1 for loop
space = O(1) fixed no.of variables"""

nums=[10,203,30,40,-10,40,98,203]
largest=float("-inf")
s_largest=float("-inf")
n=len(nums)

for i in range(0,n):
    if nums[i]> largest:
        s_largest= largest
        largest=nums[i]
        
    elif nums[i]>s_largest and nums[i]!=largest:
        s_largest=nums[i]

print(s_largest)


#using function

def find_second_largest(nums):
    largest=float("-inf")
    s_largest=float("-inf")
    n=len(nums)
    
    for i in range(0,n):
        if nums[i]>largest:
            s_largest=largest
            largest=nums[i]
            
        elif nums[i]>s_largest and nums[i]!=largest:
            s_largest=nums[i]
            
    return s_largest

nums=[10,20,30,50,80,90]

print(find_second_largest(nums))