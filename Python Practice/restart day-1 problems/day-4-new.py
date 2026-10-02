# #check palindrom or not
# string="hello"
# if string==string[::-1]:
#     print("Palindrome")
# else:
#     print("Not a Palindrome")




# #using for loop
# string=input("enter a string: ")
# reverse=""
# for char in string:
#     reverse=char+reverse


# if string==reverse:
#     print("Palind")

# else:
#     print("Not Palin")


# #using 2 pointer

# string=input() 
# # eg=hello-> 01234(index values)
# #length=5 (characters)
# #start index=0
# #end index=len(string)-1 (5-1=4)


# left=0 #start index
# right=len(string)-1

# while left<right:
#     #0<4, 0<3, 0<2, 0<1==> 0<0== false come out loop
#     if string[left]!=string[right]:
#         print("not")
#         breakpoint()

#     left+=1
#     right-=1

# else:
#     print("yes")


# #check a number is palindrom or not
# num = int(input("enter a num: "))
# original = num
# reverse=0

# while num>0:
#     digit= num%10 # to get last digit
#     reverse= reverse*10+digit # to reverse the num and strore in the reverse variable
#     num = num//10 # use to remove last digit

# if original == reverse:
#     print("Palindrome")
# else:
#     print("Not Palindrome")



# # reverse a number
# num=123 ## reverse=321
# reverse=0

# while num>0:
#     digit=num%10 # to get last digit
#     reverse = reverse*10 + digit # to reverse the num
#     num = num//10

# print(reverse)



# anagram
# str_1= input("Enter a string: ")
# str_2 = input("Enter a string: ")
# if sorted(str_1)==sorted(str_2):
#     print("Anagram")
# else:
#     print("Not")
    
    
#using for loop
# s1=input()
# s2=input()
# if len(s1)!=len(s2):
#     print("not Anagram")
# else:
#     flag=True
#     for ch in s1:
#         if s1.count(ch)!=s2.count(ch):
#             flag=False
#             break
        
#     if flag: # if flag is true
#         print("Anagram")
#     else:
#         print("Not Anagram")






# multiplication table 

# #using for loop
# n=int(input()) # in the form==> 5X1=5
# for i in range(1,11):
#     print(n, "x",i, "=", n*i )
    
    
# #using while loop
# n=int(input())
# i=1
# while i<=10:
#     print(n,"x",i,"=",n*i)
#     i+=1
    
    
    


# # swap 2 numbers:
# a,b=10,20
# a,b=b,a
# print("A Value is: ", a, "B Values is: ",b,)

# #using 3rd variable
# a=10
# b=20
# temp=a
# a=b
# b=temp

# print(a)
# print(b)




# # calculate the factorioal
# #using for loop
# n=5
# sum=1
# for i in range(1, n+1):
#     sum=sum*i
# print(sum)



# #using while loop
# n=5
# fact=1
# i=1
# while i<=n:
#     fact *=i
#     i+=1
    
# print(fact)


# # min max of three num
# a=10
# b=20
# c=30
# if a>b and a>c:
#     print(a, "is greater")
# elif b>a and b>c:
#     print(b, "is greater")
# else:
#     print(c, "is greater")


# #apraoch 2 of min max
# a=10
# b=20
# c=30
# max_num=a
# if b>max_num:
#     max_num=b
# if c>max_num:
#     max_num=c
    
# print(max_num)

# #with basic approach of min max
# a=10
# b=20
# c=30
# print(max(a,b,c))
# print(min(a,b,c))
    


# #print sum of n natural numbers
# #1 approach - for loop
# n=5
# sum=0
# for i in range(1,n+1):
#     sum=sum+i
# print(sum)



# #2 approach - while loop
# n=3
# sum=0
# i=1
# while i<=n:
#     sum=sum+i
#     i+=1
# print(sum)



# #3 approach formula method 
# n=int(input())
# total=n*(n+1)//2
# print(total)

# #print n natural numbers
# n=int(input())
# for i in range(1,n+1):
#     print(i)
    
    




