"""tuple_1=("Hello", "Pavan")

#operations on tuples
print(tuple_1[1])
print(tuple_1[-1])
print(len(tuple_1))

#concationation
new=tuple_1 + ("Kalyan",)
print(new)
print(tuple_1)

#repetition
new_1= new *2
print(new_1)

#indexing
print(new[1:3])

#index value return
print(new.index("Kalyan")) # return the index no.
"""

#================================================================


"""#new tuple
new_tuple=(1,2,3,"Pavan", "Kalyan")
#          0 1 2   3        4

#traverse
for i in new_tuple:
    print(i)
    
#================================================================

#traverse using index
for i in range(0, len(new_tuple), 2):
    print(f"index value {i} is : {new_tuple[i]}")
    
#================================================================

#traverse using index
for i in range(len(new_tuple)):
    print(f"Index {i} contain value: {new_tuple[i]}")"""
    
    
#================================================================

"""#new problems over the tuple
new_tuple=(1,2,3,"Pavan", "Kalyan")

#access the element in a tuple
print(new_tuple.index("Pavan"))

#using index
print(new_tuple[4])
"""

#================================================================


"""#adding multiple elements to the tuple
tuple_1=(1,2)
n=2 #no. of elements to add
for i in range(0,n):
    new_values= int(input("Enter elements: "))
    tuple_1 = tuple_1 + (new_values,)

print(tuple_1)"""


#================================================================


"""#find the specific element a index
new_tuple=(1,2,4,4, 6,6,56,78,99)

find=4
for i in range(0, len(new_tuple)):
    if find==new_tuple[i]:
        print(f"element {find} is at index : {i}")
        break
    
    


#================================================================


#find the occurance of a element
new_tuple=(1,2,3,4,5,55,6,32,22,333,33,3,2,5)
count=0
for i in range(0, len(new_tuple)):
    if 2==new_tuple[i]:
        count+=1
print(count)
    
#using count function
print(new_tuple.count(4))

#using the values not index
new_tuple=(1,2,3,4,5,55,6,32,22,333,33,3,2,5)
count=0
for i in new_tuple:
    if i==2:
        count+=1
print(count)



#using dict
new_tuple=(1,2,2,4,6,6,8,3,2)
count={}
for i in new_tuple:
    if i in count:
        count[i]+=1
    else:
        count[i]=1

for key,value in count.items():
    print(f"element {key} has count : {value}")


"""    


#================================================================
    