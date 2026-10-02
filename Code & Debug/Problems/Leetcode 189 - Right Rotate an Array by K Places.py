"""def rotate_array_k_place(nums,k):
    n=len(nums)
    k=k%n
    nums[:]= nums[n-k: ] + nums[ :n-k]
    
    return nums

nums=[1,2,3,4,5,6,7,8]
print(rotate_array_k_place(nums,5))"""

"""TC= O(k+n-k)= O(n)
SC= O(n) slicing use the extra space for right side"""




##optimal solution
### tc= o(n)
### sc= o(1)

nums=[1,2,3,4,5,6,7,8,9,10]
k=3
n=len(nums)
k=k%n

def reverse(left, right):
    
    while left< right:
        nums[left], nums[right]= nums[right], nums[left]
        left+=1
        right-=1
        
reverse(0, n-1)
reverse(0, k-1)
reverse(k, n-1)

print(nums)