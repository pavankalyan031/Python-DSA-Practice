"""
Control statements in Python manage the execution flow of a program based on logic, conditions, and loops. 

1. Conditional Statements (Selection):

These allow your program to choose different code execution paths based on whether a specific logic check evaluates to True or False.

if: Executes a localized block of code only if its condition evaluates to True.
else: Pairs with an if block to execute alternative logic when the tested condition is False.
elif: Short for "else if". It evaluates an additional condition if the preceding choices fail.
match: Introduced in modern Python, this provides native structural pattern matching similar to switch-case statements in other languages.

eg: 
if condition:
 statement
"""
# a=int(input())
# if a%2==0:
#     print("Even")
# elif a%2!=0:
#     print("Odd")
# else:
#     print("Enter a correct value")
    
    
    
"""
2. Iterative Statements (Looping):
Loops allow you to repeatedly run a specific block of code without rewriting it. Python offers two core iterative mechanisms

for: Best utilized when iterating through an exact range of numbers or a pre-determined collection sequence like lists, strings, or dictionaries.

while: Repeats a given code block continuously as long as its underlying logical condition remains True



"""

# for i in range(0,2):
#     print(i)
    

# a=10

# while a<3:
#     print(f"Count is {a}")
#     i+=1
    
    
"""
3. Transfer Statements (Loop Control / Jumping)

Transfer statements fundamentally alter how loops operate by skipping specific parts or exiting early.
break: Exits the closest enclosing loop immediately, skipping any remaining code or iterations.

continue: Aborts the rest of the current iteration block and moves directly to the next loop pass.

pass: A null placeholder statement that does absolutely nothing; used when syntactical rules require code but you haven't written the logic yet



"""

#break

for a in range(1,10):
   if a==4:
       break
   print(a) 
    
print()
#continue
for i in range(1,6):
    if i==4:
        continue
    print(i)