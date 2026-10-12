#brute force - 
# tc= O(n(n+1)) = O(n**2)
#sc= O(1)

def sumoftwo(nums):
    n=len(nums)
    # target= 13
    for i in range(0, n-1):
        for j in range(i+1, n):
            if nums[i]+ nums[j]==target:
                return [i, j]

nums = [2,7,11,15]
target = 9
print(sumoftwo(nums))

