# # # 1. number is even or odd
# # n=10
# # if n%2==0:
# #     print("even")
# # else:
# #     print("odd")
    
    
# # n=9
# # if n%2!=0:
# #     print("odd")
# # else:
# #     print("even")
    
    
    
# # n=10
# # print(n%2==0)
    
    
    

# # def check(n):
# #     if n%2==0:
# #         print("even")
# #     else:
# #         print("odd")

# # check(10)


# # def check(n):
# #     return n%2==0

# # result=check(2)
# # print(result)


# # n=10
# # print("Even" if n%2==0 else "Odd")

# # n=10
# # if n & 1==0:
# #     print("Even")
# # else:
# #     print("Odd")
    
    
    
    
    


# # # 2. print n natural numbers
# # # using for loop
# # for i in range(1,10):
# #     print(i)
    

    
# # n=5   
# # for i in range(1,n+1):
# #     print(i)
    
    
    
    
# # # using the while loop
# # n=10
# # i=1
# # while i<=10:
# #     print(i)
# #     i+=1
    
    

# # 3. print any string n times using loops

# # using for loop
# text ="hello"
# n=5
# for i in range(n):
#     print(text)
    
    
# # using while loop
# text="hi"
# n=10
# i=1
# while i<=n:
#     print(text)
#     i+=1
    
    
# # normal method
# text="hello\n"
# n=3
# print(text * n, end ="")


# for i in range(3):
#     print(i, end=" ")
    
    
# print("Hello", end="\n")
# print("World")


# text="Hello"
# for i in range(1):
#     print(text)



# print each character from given string
text="Hello"
for char in text:
    print(char)
    
    
text="Python"
i=0
while i<=2: # i<len(text) print(text[i]) i+=1
    print(text)
    i+=1
    
    
text="Hello"
for i in range(len(text)):
    print(text[i])
    
    


#check if two strings are anagrams
text1="ra"
text2="care"
if sorted(text1)==sorted(text2):
    print("anagram")
else:
    print("not anagram")
    