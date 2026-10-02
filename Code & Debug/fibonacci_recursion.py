#fibonacci : f(n)= f(n-1)+f(n-2)

def fib(n):
      if n<=1: #if n is 0 or 1:
         return n
      return fib(n-1)+fib(n-2)

print(fib(5))