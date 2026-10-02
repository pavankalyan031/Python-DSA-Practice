#type conversion 
#1. string --> int add 50 and print result

a="10"
b=int(a)
b+=50
print(type(b))
print(b)



#relational operators
#2. greater and smaller

num1=10
num2=20
if num1>num2:
    print("num1 is greater")
elif num2>num1:
    print("num2 is greater")
else:
    print("Both are equal")
    
    
    

#logical operators

age = 19
has_license=True
if age>18 and has_license:
    print("Can drive")
else:
    print("Cannot drive")
    
    
    
#assignment operator
count=10
count+=5
print(count)




#type conversion
float_price=19.99
print(round(float_price)) #math.floor(19.99)--> down = 19 #math.ceil(19.99)--> up = 20
