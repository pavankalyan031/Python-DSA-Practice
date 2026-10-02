nums=[1,2,3,4,5,6,7]
n= len(nums)
temp= nums[n-1]
k=3
while k<=3: 
    for i in range(n-2, -1, -1):
        nums[i+1]= nums[i]
        
    nums[0]=temp
    
return nums
    

print(rotate_array(nums))