#brute force
def max_subarray(nums):
    n=len(nums)
    current_sum=nums[0]
    max_sum= nums[0]

    for i in range(0,n):
        if current_sum < 0:
            current_sum= nums[i]
        else:
            current_sum+= nums[i]

            if current_sum> max_sum:
                max_sum= current_sum

    return max_sum


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_subarray(nums)) 