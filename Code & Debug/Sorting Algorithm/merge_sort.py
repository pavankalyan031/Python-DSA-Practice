def merge_sort(array):
    if len(array)<=1:
        return array ##base condition as its a recursion baased
    
    mid = len(array)//2
    
    left_half= array[:mid]
    right_half= array[mid:]
    
    left= merge_sort(left_half)
    right= merge_sort(right_half)
    
    return merge_array(left, right)
    
    
def merge_array(left, right):
    result=[]
    i=0
    j=0
    
    while i<len(left) and j<len(right):
        if left[i] <= right[j]:
                result.append(left[i])
                i+=1
        else:
            result.append(right[j])
            j+=1
            
    #result.extend(left[i:])
    #result.extend(right[j:])
    
    #or
    
    
    while i<len(left):
        result.append(left[i])
        i+=1
    while j<len(right):
        result.append(right[j])
        j+=1
        
    
    return result


array=[3,2,1,4,4,2,4,8,1]
print(merge_sort(array))