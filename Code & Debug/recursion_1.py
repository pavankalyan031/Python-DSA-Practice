"""Recursion is a programming technique in which a function calls itself to solve a
smaller instance of the same problem until it reaches a base case, where the
recursion stops."""

# recursion infinite loop
def fun(n):
    if n== 0:
        return
    print("Pavan")
    fun(n-1)
fun(4)