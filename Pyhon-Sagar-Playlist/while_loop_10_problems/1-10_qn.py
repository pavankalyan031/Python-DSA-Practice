"""
14. Interview Questions

Beginner

Print 1 to N
Print N to 1
Sum of first N numbers
Multiplication table
Count digits
Reverse a number
Sum of digits
Product of digits
Even/Odd numbers
Print alphabets

Intermediate

Palindrome Number
Armstrong Number
Prime Number
GCD
LCM
Fibonacci
Decimal → Binary
Binary → Decimal
Power using loop
Factorial

Advanced (FAANG)

Arrays
Reverse Array
Two Sum (sorted)
Remove Duplicates
Move Zeroes
Binary Search
Binary Search
First/Last Occurrence
Search Insert Position
Peak Element
Sliding Window
Longest Substring Without Repeating Characters
Minimum Size Subarray Sum
Linked List
Reverse Linked List
Detect Cycle
Trees & Graphs
BFS
DFS
Level Order Traversal
Recursion Simulation
DFS using explicit stack

"""
"""#1. print 10-15 mumber
n=10
while n<=15:
    print(n, end=" ")
    n+=1
    



#2. print cubes of 1-5 like 1, 8, 27...
n=1
while n<=5:
    print(n **3, end=" ")    
    n+=1
    


#3. print odd number from 1-10
n=1
while n<=10:
    if n%2!=0:
      print(n, end=" ")
    n+=1




#4. calculate the products of 1-5
#eg: 1*2*...=120
num=1
product=1
while num<=5:
    product*=num
    num+=1
print(product)



#5. reverse each word in a sentence
#eg: Hello World
#==> olleH dlroW

sentence= "Hello World"
character= sentence.split()

for char in character:
    i=len(char)-1
    while i>=0:
        print(char[i], end="")
        i-=1
        
    print(end =" ")
print() 


 
#using for loop
sentence_1="Hello Pavan"
for char in sentence_1.split():
    for i in range(len(char)-1, -1, -1):
        print(char[i], end="")
    print(end=" ")
    
    


#6. count consonants in a string of learning
#using for loop
string="Hello"
count=0
for char in string: #.lower()
    if char not in "aeiou": #.isalpha() and char
        count+=1
print(f"Consonants are : {count}")


#using while loop 
string_1= "Pavan"
vowels="aeiou"
count=0
i=0
while i<len(string_1):
    if string[i] not in vowels:
        count+=1
    i+=1
print(f"Consonants are : {count}")





#7. print the first 5 multiples of 3
#eg: 1 3 6 9 15

#using for loop
count=0
for i in range(1,100):
    if i%3==0:
        print(i, end=" ")
        count+=1
    if count==5:
        break
    
    
#using while loop
i=1
count=0
while count<5:
    if i%3==0:
        print(i, end=" ")
        count+=1
    i+=1
    
    
#simple approach
#for loop
for i in range(1,6):
    print(3*i, end=" ")

#while loop
count=1
while count<=5:
    print(3*count, end=" ")
    count+=1
    
print()  
#using like 3 X 1 = 3 like this 
count=1
num=3
while count<=5:
    print(f"{num} X {count} = {3*count}")
    count+=1
    


#calculate the power of a num 
#eg: base =3, exponent=4
#output is = 81
base=3
exponent=4
result=1
count=0
while count<exponent:
    result*=base
    count+=1
print(result)



#using for loop
base=3
exponent=4
result=1
for i in range(exponent):
    result*=base #result= result*base # 1=1*3 ==> 3 then 3=3*3 ==> 9 like this till 27=27*3 ==> 81
print(result)



# check if a num is a perfect square
#eg: 16 => yes perfect square

#using for loop
num=int(input("enter a perfect square: "))
perfect=False
for i in range(1, num+1):
    if i*i==num:
        perfect=True
        break
if perfect:
    print(f"{num} is a perfect square")
else:
    print(f"{num} is not a perfect square")
    


#using while loop
num=int(input("Enter a perfect square num: "))
perfect=False
i=1
while i<=num:
    if i*i==num:
        perfect=True
        break
    i+=1
    
if perfect:
  print(f"{num} is a perfect square")  
else:
    print(f"{num} is not a perfect square")
    
    
# approach 2
num=int(input("Enter a num: "))
i=1
while i<=num:
    if i*i==num:
        print("Perfect Square")
        break
    i+=1
else:
    print("Not Perfect Square")
    
# using normal approach
num=int(input("Enter a num: "))
square= int(num**0.5)

if square*square==num:
    print("Perfect")
else:
    print("Not perfect")
    
    



#count occurence of a specific character in a string
#eg: s in string "success"
#input=success
#output=s:3

string="success"
character=input("Enter a character to find: ")
count=0
i=0
while i<len(string):
    if string[i]==character:
        count+=1
 
    i+=1
print(f"{character} : {count}")


#using for loop
string="Success"
character=input("Enter a char to find: ")
count=0
for char in string:
    if char.lower() == character:
        count+=1
print(f"{character} : {count}")


"""