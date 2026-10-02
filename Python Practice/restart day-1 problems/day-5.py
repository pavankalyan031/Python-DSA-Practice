# #list
# my_list=[1,2,3,4,5]
# print(my_list)



# #using for loop
list_1=[]
n= int(input("enter no.of items: "))
for i in range(0,n):
    value=int(input("enter a value: "))
    list_1.append(value)
    
print(list_1)
 
#append
my_list=[1,2,3,4,5,6]
my_list.append(10)
print(my_list)


#update 
my_list[2]=200
print("updated list", my_list)


#traverse
for i in my_list:
    print(i)
    
    
#insert 
my_list.insert(4,1000)
print("inserted", my_list)


#extend--> add list in another list
my_list.extend([1111,2222])
print("extended", my_list)


#=+ operator
my_list +=[11111111,2,2222,0]
print("new list", my_list)


#remove a specific element
my_list.remove(1)
print(my_list)


#pop for specific index element --> not mentioned means remove last one 
my_list.pop()
print(my_list)

#specific index pop
my_list.pop(1)
print(my_list)


list=[1,2,3]
print(list)