"""# bubble sort
def bubble_sort(arr):
    n=len(arr)
    for i in range(0, n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1]= arr[j+1], arr[j]
                
    return arr

arr=[5,1.4,2,8]
print(bubble_sort(arr))

#Time complexity = O(n(n-1)) == O(n*2)
#Space complexity = O(1) --> no extra space is used
"""

def bubble_sort(array):
    n=len(array)
    for i in range(n-1):
        swapped= False
        for j in range(n-i-1):
            if array[j]> array[j+1]:
                array[j], array[j+1]= array[j+1], array[j]
                swapped= True
        
        if not swapped:
            break
        
    return array

array=[1,4,13,19,2]
print(bubble_sort(array))

#Time complexity = O(n) --> if array is sorted means no swapped
#Space complexity = O(1)
