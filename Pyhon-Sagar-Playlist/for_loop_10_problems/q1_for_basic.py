"""#1. print number 1-5 using for loop
for i in range(1, 6):
    print(i, end=" ")
    """


"""#2. print square of 1-5
for i in range(1,6):
    print(i*i, end=" ")   #i**2 """
    
    
"""#3. print even number 1-10
for i in range(1,11):
    if i%2==0:
        print(i, end=" ")"""
        
        
"""#4. calculate the sum of 1-10 number
sum=0
for i in range(1,11):
    sum+=i # sum=sum+i
print(f"Sum is = {sum}")"""
     
     
"""#5. reverse a word
str_1="Python"
for char in str_1[::-1]:
    print(char, end="")

print()
#method 2
str_2="Python"
for i in range(len(str_2) -1, -1, -1):
    print(str_2[i], end="")
        
"""





"""#6. count the vowels in a string
vowel="aeiou"
word="education"
count=0
for char in word:
    if char in vowel:
        count+=1
        
print(count)"""




#7. fibonacci series up to 10 terms
#each term in the fibonacci series is teh sum of the 2 proceding ones
"""
"""#eg : 1st- 0, 2nd- 1, 3rd- 0+1=1, 4th-2nd+3rd term means 1+1=2, like this """
"""n=int(input("Enter the number: "))
a=0
b=1
for i in range(n):
    print(a, end=" ")
    a=b
    b=a+b"""
    #temp=a+b
    #a=b
    #b=temp"""
    
    
    
    
"""#8. factorial 
n=5
fact=1
for i in range(1, n+1):
    fact = fact*i
print(f"factorial is : {fact}")"""


#9. check prime numbers
"""n=int(input("Enter a num to check: "))
if n<=1:
    print("Not Prime")
    
else:
    prime= True
    for i in range(2, n):
        if n%i==0:
            print("Not Prime")
            break
    else:
        print("Prime")
    """
    
# 9/2. print n prime numbers
"""n=int(input("Enter the num: "))
for i in range(1, n+1):
    if i<=1:
        continue
    prime = True
    for j in range(2, int(i**0.5)+1):
        if i%j==0:
            prime = False
            break
    if prime:
        print(i, end=" ") """
    

#9. using function 
"""def is_prime(num):
    if num<=1:
        return False
    
    for i in range(2, int(num**0.5)+1):
        if num%i==0:
            return False
    
    return True

n=int(input("Enter a num: "))
for num in range(1, n+1):
    
    if is_prime(num):
        print(num, end=" ")"""
        
        
#10. count the occurence of the word:
"""
eg: programming => p :1, r: 2 ,.....
"""

word="programming"
count={}
for i in word:
    if i in count:
        count[i]+=1
        
    else:
        count[i]=1
        
#print(count)
for key, value in count.items():
    print(key, ':', value)