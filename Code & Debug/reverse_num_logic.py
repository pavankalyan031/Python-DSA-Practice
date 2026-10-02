"""#1. reverse a num
num=5673
while num>0:
    last_digit=num%10
    print(last_digit,end="")
    num=num//10
    
    """

"""#2. count digits in an integer
n=103334 #6
num=n
count=0
while num>0:

    num=num//10
    count+=1

print(count)


#using function 
def count_digits(n):
    count=0
    while n>0:
        
        n=n//10
        count+=1
    return count
    
    
print(count_digits(101010))"""


"""#3. check palindrome
n=121
num=n
result=0
while num>0:
    last=num%10
    result=(result*10)+last
    num= num//10
if n==result:
    print("Pal")
else: print("Not Pal")

#using function

def check_pal(n):
    num=n
    result=0
    while num>0:
        last=num%10
        result=(result*10)+last
        num= num//10
    if n==result:
        print("Pal")
    else:
        print("Not")
        
n=1234
check_pal(n)"""


"""#4. armstrong num
#eg: n=153 ==> no. of digits d is 3 
# so, each raise power of d in each num then sum each 
# 1**3+5**3+3**3=152 compare if n== new num then armstrong num
n=int(input("Enter a num to check: "))
num=n
total=0
#no.of digits means how many numbers of count length
nod=len(str(n))
while num>0:
    last_digit=num%10
    total=total+ (last_digit**nod)
    # 0+(3**3)=27 like this 27+125+1=153
    num//=10
if total==n:
    print(f"{n} is armstrong num")
else:
    print(f"{n} is not armstrong num")"""
    
    
    
    

#4. print all factors/divisors of a number
num=int(input("Enter a num: "))
result=[]
for i in range(1, num+1):
    if num%i==0:
        result.append(i)

print(result)


#approach 2 is by n//2 which check half of its number 
#eg: 10 = 1,2,3,4,5,6,7,8,9,10 but factors are : 1,2,5,10 
#here we are gettig till half and main num
n=10
result=[]
for i in range(1,(n//2)+1):
    if n%i==0:
        result.append(i)

result.append(n)
print(result)