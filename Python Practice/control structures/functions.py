# #function is a block of code it run when it called, we can pass the data within the () called as parameters
# # a function can return data as a result

# def my_function():
#     print("hello pavan")
    
# my_function()



# def hello(name):
#     print("hello bro " + name)
    
# hello("Pavan")



# def square(n):
#     return n*n

# r=square(10)
# print(r)





# def q(n):
#     return n**2
# print(q(5))



# def f(n):
#     return n**2
# result = f(5)
# print(result)


# f= lambda x: x**2

# result = f(10)
# print(result)







#method 1
def add(a1,b1):
    print(a1+b1)
    
a= int(input("enter a value: "))
b= int(input("enter a value: "))

add(a,b)
breakpoint()


# method 2
def add(a1, b1):
    return a1+b1

a1 = int(input("enter a value: "))
b1 = int(input("enter a value: "))

answ = add(a1,b1)
print(answ)