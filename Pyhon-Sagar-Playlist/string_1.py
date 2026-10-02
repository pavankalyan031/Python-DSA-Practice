"""# 1. access element one by one 
string = "Hello Pavan"
l=len(string)
i=0
while i<l:
    print(string[i], end=" ")
    i+=1
    
print()
    
# reverse element to print
string_1="hello bro"

i=1
l_1=len(string_1)
while i<=l_1:
    print(string_1[-i], end=" ")
    i+=1
    
    
    
"""
#reverse using for loop
a="Hello"
for i in a[::-1]:
    print(i, end=" ")
    
print()  
# general questions
#1. count string in main string
a="hello"
b=a.count("o") #1
print(b)


#2. strip() remove the space extra
a=" Hello "
print(a) #_Hello_

print(a.strip()) #Hello
print(a.lstrip()) #Hello_