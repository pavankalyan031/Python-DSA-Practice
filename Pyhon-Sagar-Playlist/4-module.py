# # import keyword
# # print(keyword.kwlist)


# a=1+2j
# print(type(a))


# #list
# a=[0]*7
# print(a)


# a=[1,2,3]
# a.insert(1,0)
# print(a)


# #extend
# a=list("GFG")
# a.extend([10])
# print(a)


# #update
# a=[1,2,3]
# a[2]=2000
# print(a) #[1,2,2000]

# #remove --> remove(), pop()
# a=[1,2,3]
# a.remove(1)
# print(a)

# #using pop
# a=[1,2,3]
# a.pop() # [1,2]
# a.pop(1) #index remove place ==> 2 is removed since in 2 in index 1
# print(a)


# #iterating
# a=[1,2,3]
# for i in a:
#     print(i)
    
    
# #del statement to del at aprticular index
# a=[1,2,3]
# del a[1]
# print(a)


# #clear() --> removes all items
# a=[1,2,3]
# a.clear()
# print(a)


# #iteration
# #while loop
# a=[1,2,3]
# i=0
# while i<len(a):
#     print(a[i])
#     i+=1
    
    
    
# #using enumerate
# a=[1,2,3]
# for i, val in enumerate(a):
#     print(i,val)
    
# #list comprehension
# a=[1,2,3]
# b= [val for val in a]
# print(b)


# #loop & range
# a=[1,2,3]
# for i in range(len(a)):
#     print(a[i])
    
    
# # string
# a="aBCD"
# b="A" + a[1:]
# print(b)
# print(a)



# #del string
# a="abc"
# del a
# print(a)

# a="abc"
# b="def"
# print(a+" "+b)


# a='hello'
# print(a*3)


# #string formating
# name='pavan'
# age=20
# print(f"Name : {name}, Age: {age}")



# #split()
# a="abc cds"
# print(a.split())
# print(type(a))

# a='abc'
# b=list(a)
# print(b)


# # reverse a tuple
# def reverse_tup(a):
#     temp=list(a)
#     left=0
#     right=len(temp)-1
#     while left<right:
#         temp[left], temp[right]= temp[right], temp[left]
#         left+=1
#         right-=1
#     return tuple(temp)

# a=(1,2,"pavan")
# print(reverse_tup(a))


# #using for loop
# def reverse_tuple(a):
#     result=()
#     for i in range(len(a)-1, -1,-1):
#     #let say len=5 but index is 5 so, we are traversing using index
#     #-1 is for stop which exclude last index means upto 0 index
#     #-1 step is used to traverse one by one element
#         result+=(a[i],)
#     return result
# a=(1,2,3)
# print(reverse_tuple(a))





# #dictionay:
# #create
# dict={'a':1, 'b':2}
# print(dict)

# 2 nd way
a= dict(name="pavan", age=20)
print(a)
print(type(a))

#acces
print(a["name"])
print(a.get("age"))


#adding & updating
a["height"]=9.6
a["height"]=10.10


#removing items
del a['name']
print(a)

#pop() - del key and return value
value=a.pop("age")

print(value)
print(a)


#pop item ==> removes and return last inserted key & value
n={'a':1, 'b':2}
# n['d']=10
print(n.popitem())
print(n)


n.clear()
print(n)

#update 
n.update({
    'a':1,
    'b':2
})
print(n)

#set default == > is exit return or create new
n.setdefault("name","pavan")
new=n.copy()




#dict methods
#keys()
n.keys()

#values
n.values()

#items()
n.items()

#get()
n.get("name")


#update()
n.update({
    'age':20
})


#max 
print(max(n))

#min
print(min(n))

#shallow copy
a={'name':'pavan', 'age': 20}
new= a.copy()
print(a,"\n", new)


#deep copy
import copy
new_1=copy.deepcopy(n)
print(new_1)



"""15. Hash Map Patterns (MOST IMPORTANT)

These are the patterns you will use repeatedly in DSA.

Frequency Count ⭐⭐⭐⭐⭐
nums = [1,2,2,3,1]

freq = {}

for num in nums:

    freq[num] = freq.get(num,0)+1

print(freq)

Output

{
1:2,
2:2,
3:1
}
Duplicate Detection ⭐⭐⭐⭐⭐
seen = {}

for num in nums:

    if num in seen:
        print("Duplicate")

    seen[num] = True
Character Count
word = "google"

count = {}

for ch in word:
    count[ch] = count.get(ch,0)+1
Grouping
students = {

"A":["Math","Science"],

"B":["English"]

}
Mapping
phone = {

"John":98765,

"David":98766

}


17. Common Interview Questions

✅ Frequency Counter

✅ First Non-Repeating Character

✅ Two Sum

✅ Valid Anagram

✅ Contains Duplicate

✅ Majority Element

✅ Intersection of Arrays

✅ Top K Frequent Elements

✅ Longest Consecutive Sequence

✅ Group Anagrams

Every one of these uses a dictionary (hash map)

✅ Frequency Counting
✅ Hashing Pattern
✅ Counting Characters
✅ Duplicate Detection
✅ Mapping
✅ Grouping
✅ Memoization
✅ Prefix Hashing
✅ Hash Maps in Graphs"""


