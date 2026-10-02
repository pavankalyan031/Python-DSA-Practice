def partition(array, low, high):
    pivot = array[low]
    i=low
    j=high
    
    while i<j:
        
        while i<=high and array[i]<=pivot:
            i+=1
        
        while j>=low and array[j]>pivot:
            j-=1
            
        if i<j:
            array[i], array[j]=array[j], array[i]
            
    array[low], array[j]= array[j], array[low]
    
    return j


def quick_sort(array, low, high):
    if low<high:
        
        #partition_index = pi
        
        pi= partition(array, low, high)
        
        quick_sort(array, low, pi-1)
        quick_sort(array, pi+1, high)
        
    return array

array= [10,7,8,9,1,5]

print(quick_sort(array, 0, len(array)-1))