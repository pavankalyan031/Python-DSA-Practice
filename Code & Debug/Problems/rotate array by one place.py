def rotate_array(nums):
    n= len(nums)
    temp= nums[n-1]
    for i in range(n-2, -1, -1):
        nums[i+1]= nums[i]
        
    nums[0]=temp
    
    return nums
    
nums=[1,2,3,4,5,6,7]
print(rotate_array(nums))