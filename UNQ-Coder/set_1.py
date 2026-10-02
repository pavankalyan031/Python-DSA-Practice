"""
A set is a collection of unique elements which does not 
support duplicate elements like lists and tuples. 
Another important point about Sets is that they are unordered, 
which makes accessing their elements using indexes impossible.


Important points about Sets:
1. A set is enclosed by {}.
2. It is a mutable data type and is iterable.
3. Even though a set is mutable, due to its no duplicates policy and unordered nature, the elements of a set are immutable.
4. We can add or delete elements from a set, but we can't perform slicing or indexing operations on a set.

5. There is another category of immutable sets called the Frozen sets.

6. Internally, the elements in a set are arranged based on hashing and hash tables.

7. If more than one element is placed in an index, the values are arranged in a linked list to that index position.

8. A set won't allow mutable items as its elements like lists.

"""
#creating set
set_a={1,2,3,4,44,5,3,23}
set_b={43,4,2,3}

print(f"Set a : {set_a}\nSet b: {set_b}")

#add element
set_a.add("Pavan")
set_a.add((1,2,3,43))
print(set_a)


#remove
set_a.remove(44)
set_a.discard(43)
print(set_a)


# #adding list
# # TypeError: unhashable type: 'list' because>>>
# set_a.add([1,2,3])


