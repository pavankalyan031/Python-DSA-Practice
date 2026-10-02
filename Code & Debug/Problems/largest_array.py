"""find the largest element in an array"""
nums=[10,203,4,0,-10,20]

#python most smallest number = -infinity ==> float("-inf")
# largest = float("-inf")find 
largest= nums[0]
n= len(nums)
for i in range(0,n):
    # if nums[i]> largest:
    #     largest= nums[i]
    largest= max(largest, nums[i])
        
print(largest)

#time = o(n)
#space = o(1)