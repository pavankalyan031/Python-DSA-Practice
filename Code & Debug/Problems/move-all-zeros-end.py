"""def non_zero(nums):
    n=len(nums)
    j=0
    for i in range(0, n):
        if nums[i]!=0:
            nums[j]=nums[i]
            j+=1
    
    while j<n:
        nums[j]=0
        j+=1
    
    return nums
     
nums=[1,0,3,0,12]
print(non_zero(nums))"""




#approach of brute force - 2
# tc- o(2n) similar to o(n)
# sc- o(n) since used temp list

"""#approch - 2
def nonzeroend(nums):
    n=len(nums)
    temp=[]
    for i in range(0,n):
        if nums[i]!=0:
            temp.append(nums[i])
    
    n1=len(temp)
    for i in range(0, n1):
        nums[i]=temp[i]
        
    for i in range(n1, n):
        nums[i]=0
        
    return nums

nums=[1,0,3,0,12]
print(nonzeroend(nums))"""





"""# optimal approach - 3
# nums= [1,0,3,0,12]
def nonzero(nums):
    n=len(nums)
    
    if len(nums)==1:
        return 
    
    j=0
    for i in range(0, n):
        if nums[i]!=0:
            nums[i], nums[j]= nums[j], nums[i]
            j+=1
            
    return nums

nums=[1,0,3,0,12]
print(nonzero(nums))"""



#another optimal approach
def nonzero(nums):
    n=len(nums)
    i=0
    j=0
    
    while j<n: #len(nums)
        if nums[j]!=0:
            nums[i], nums[j]= nums[j], nums[i]
            i+=1
        
        j+=1
        
        