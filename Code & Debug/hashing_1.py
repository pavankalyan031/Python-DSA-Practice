"""
Interview Cheat Sheet
Question	One-Line Answer
What is Hashing? ==>	Technique to map keys to indexes for fast access.
Hash Function ==>	Converts a key into an index.
Hash Table ==>	Data structure storing data at hashed indexes.
Collision ==>	Two keys map to the same index.
Collision Resolution ==>	Chaining and Open Addressing.
Chaining ==>	Store collided elements in a linked list (or list) at the same index.
Open Addressing	Find another empty slot in the table.
Load Factor ==>	Number of elements ÷ table size.
Why O(1)? == >	Direct access using the hash function.
Why O(n)? ==>		Many collisions force sequential searching.
Python dict ==>		Hash table storing key-value pairs.
Python set ==>		Hash table storing unique keys.
When to Use Hashing? ==>		Fast lookup, duplicates, frequencies, membership, and pair-finding problems.
Good Hash Function ==>		Fast, deterministic, uniformly distributed, and minimizes collisions.
Why Not Sorted? ==>		Elements are placed according to their hash index, not their natural order.
"""

#count of m in n occurance
n=[1,2,3,5,6,7,8,10]  
m=[10, 222, 33 ,3,3,40, 2,4]
count=0
for num in m:
    count=0
    for x in n:
        if x==num:
            count+=1
    print(count)
    
    
print()


#using hashing
n=[1,2,3,5,6,7,8,10]  
m=[10, 222, 33 ,3,3,40, 2,4]
hash_list=[0]*11 
for i in n:
    hash_list[i]+=1
for j in m:
    if j<1 or j>10:
        print(0)
    else:
        print(hash_list[j])
        

print()

#using hashing in dict
n=[1,2,3,5,6,7,8,10]  
m=[10, 222, 33 ,3,3,40, 2,4]
freq_map={}
for i in n:
    freq_map[i]=1 #freq_map={1:1, 2:2, ....}
for j in m:
    if j in freq_map:
        print(j)
        del freq_map[j]
        
print()       

#count m in n occurance in how many times
n=[1,2,3,5,6,7,8,10]  
m=[10, 222, 33 ,3,3,40, 2,4]
freq_map={}
for i in n:
    if i in freq_map:
        freq_map[i]+=1
    else:
        freq_map[i]=1
        
for j in m:
    print(freq_map.get(j, 0))