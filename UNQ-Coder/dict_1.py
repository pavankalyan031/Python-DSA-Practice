"""
"A dictionary is a collection of {key: value} pairs. 
Keys map values, and to access the values, in the places of indexes, we need to use the keys. 
It is an unordered collection of data.
"Important Points About a DictionaryKey Properties: 

1. Keys identify values. Hence, a key has to be unique and immutable. 
2. Only immutable data types are accepted to be keys.
3. Value Flexibility: Any data type can be used to make a value as it is the data.
4. Duplicate Restrictions: There cannot be any duplicate keys, but duplicate values are allowed.
5. Creation Method: We can also use dictionary comprehension to create a dictionary like list comprehension.
6. eg: Real-World Analogy: The dictionary's keys are like the Roll numbers of students, and the values are the students' names.
"""

#create 
dict_1={
    '1': 'Pavan',
    "2": "Kalyan",
    "3": "Rahul"
}
print(dict_1)

#add an item
dict_1['4']="Nanna"
print(dict_1)

print(dict_1.values())

print(dict_1.keys())


#travers
for key, values in dict_1.items():
    print(f"{key} : {values}")
    
#pop
dict_1.pop("1")
print(dict_1)


#clear
dict_1.clear()
print(dict_1)


#functions
#.get()

dict_1={
    '1': 'Pavan',
    "2": "Kalyan",
    "3": "Rahul"
}

print(dict_1.get("1"))


#.update()
new={'3': 'Amma'}
dict_1.update(new)
print(dict_1)


