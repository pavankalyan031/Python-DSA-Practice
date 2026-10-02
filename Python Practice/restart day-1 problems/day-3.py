# #check number is evn or odd
# n=10
# if n%2==0:
#     print("Even")
# else:
#     print("Odd")


# #using t/false
# num= int(input("enter a num: "))
# print(num%2==0)


# #using bitwise last digit 1--> odd and last digit 0--> even
# # example--> 2==> 8421--> 0010 and for 3--> 0011

# n=10
# if n & 1:
#     print("Even")
# else:
#     print("Odd")



# #using function
# def is_even(num):
#     print(num%2==0)

# is_even(10)


# def _is_odd(num):
#     return num%2==0

# print(_is_odd(10))



# #using bitwise

# num = int(input("Enter a num: "))
# if num & 1:
#     print("Odd")
# else:
#     print("EVen")





# # n natural number:
# n=int(input("Enter a num: "))
# for i in range(1, n+1):
#     print(i)   



# # using while 
# n=10
# i=9
# while i<=n:
#     print(i)
#     i+=1


# # store in a list
# n=10
# num=[]
# for i in range(1, n+1): # range(start, stop, step) --> #negative range(10, 0,-1)--> 10 9 8...
#     num.append(i)

# print(num)



# # print any input string n times using loops
# # example --> need input string and n for number of times 
# text= "Hello"
# n= int(input("Enter: "))
# for i in range(n):
#     print(text)


# # using while loop
# text="hi"
# n=3
# count=1
# while count<=n:
#     print(text)
#     count+=1


# #using string multiplication
# text="hello"
# n=3
# # print((text+"\n")*n, end="") 
# print("\n".join([text]*n))



# #4. reverse a string
# # menthod - 1 using string slicing
# text="hello"
# print(text[::-1])


# # method 2 => for loop
# text="hello"
# result=""
# for char in text:
#     result = char+result

# print(result)


# #using while loop
# text="hi"
# i=len(text)-1

# while i>=0:
#     print(text[i],end="")
#     i-=1





