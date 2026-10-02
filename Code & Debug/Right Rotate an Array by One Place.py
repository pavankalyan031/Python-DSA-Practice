def rotate_array(arr):
    n=len(arr)
    temp=arr[n-1]
    for i in range(n-2, -1, -1):
        arr[i+1]=arr[i]
        
    arr[0]=temp
    
    return arr

arr=[1,2,3,4,5,6,7]
print(rotate_array(arr))