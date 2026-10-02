list_1=[1,2,3,4]
print(list_1)


# adding element
#append
list_1.append(10)
print(list_1)


#insert at specific position
list_1.insert(2,101)
print(list_1)



#add a list in another list
list_1.extend([10,20])
print(list_1)


#remove element by a value
list_1.remove(10)
print(list_1)


#removing at a specific element by index
list_1.pop(1)
print(list_1)



#clear the elements of the list
list_1.clear()
print(list_1)



list_2=[1,2,3,4,5]
print(list_2)


#slicing of list
new_list= list_2[1:4]
print(new_list)



#reverse the list
reverse_list=list_2[::-1]
print(reverse_list)



#sorting the list
list_2.sort()  #new_sort= list_2.sort()
print(list_2)  #print(new_sort)


#iterating list by value
list_3=[1,2,3,4,5]
for item in list_3:
    print(item)
    
    
#iterating by index just indexes
for i in range(len(list_3)):
    print(i)
    
    
#using list index values
for i in range(len(list_3)):
    print(list_3[i])
    
    
#enumerate => index, value
list_4=[1,2,3,4,5]
for index, values in enumerate(list_4):
    print(index, values)
    


#finding length
print(len(list_4))
    

#finding min and max values   
print(max(list_4))
print(min(list_4))






