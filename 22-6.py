# Problem 2: Find the Largest and Smallest Element in a List

# Write a function that takes a list of integers and returns the largest and smallest element.

# Example
# Input:
# [2, 5, 1, 3]

# Output:
# Largest = 5
# Smallest = 1


# simple approach 
def find_maximum(num):
    return max(num)

num=[1,2,3,4]
print(find_maximum(num))



#using 2nd approach - interview based

def max_finder(num):
    largest=num[0]
    smallest=num[0]
    for i in num:
        if i>largest:
            largest=i
        if i<smallest:
            smallest=i
    return largest, smallest

num=[2,5,1,3]
largest, smallest=max_finder(num)
print("largest: ", largest)
print("smallest: ", smallest)