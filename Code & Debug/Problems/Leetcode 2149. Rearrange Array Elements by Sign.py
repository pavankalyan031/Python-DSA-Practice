# #tc= O(2n)== O(n)
# #sc= O(n)

# class Solution:
#     def rearrangeArray(self, nums: list[int]) -> list[int]:
#         n= len(nums)
#         result= []
#         positive_num= []
#         negative_num= []

#         for i in range(0, n):
#             if nums[i]>0:
#                 positive_num.append(nums[i])
            
#             else:
#                 negative_num.append(nums[i])

#         for j in range(len(positive_num)):
#             result.append(positive_num[j])
#             result.append(negative_num[j])

#         return result
                

# nums=[1,-2,3,-4,5,-6]
# a1= Solution()
# print(a1.rearrangeArray(nums))




#tc = O(n)
#sc= O(n)
#Optimal Solution

def rearrangeArray(nums):
    n= len(nums)
    result= [0]*n
    p_index= 0
    n_index= 1

    for i in range(0,n):
        if nums[i]>=0:
            result[p_index]= nums[i]
            p_index+=2
        else:
            result[n_index]= nums[i]
            n_index+=2

    return result

nums= [1,-2,-3,-4, 9,10,]
print(rearrangeArray(nums))