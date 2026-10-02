str="pavan"
b=str.replace("pavan", "kalyan")
print(str)
print(b)



"""operators - operators are special symbols that performm operations on variables and values
eg= 5+2=7 --> operation
5,2 --> operands
+ --> operator

An Expression is a combination of

Operands
Operators

that produces a value.
eg: 5+3=8 this entire is called expression

1. arthimetic ==> +,-,*,%, /, //,**
2. assignment ==> =

+=

-=

*=

/=

//=

%=

**=
eg: a=10

3. comparison:
==

!=

>

<

>=

<=
return True or False


4. logical: 
and
or 
not

5. bitwise:
&

|

^

~

<<

>>

6. identity: They are used to check if two variables refer to the exact same object in memory, rather than just checking if their values are equal
is, 
is not
eg:
a=10
b=10
c=a
print(a is b)
print(a is c)
print(a is not b)
7. membership: to test whether a specific value or variable exists within a collection or sequence. 
in 
not in 

eg: 
a=[1,2,3,4]
print(2 in a)
print(5 not in a)
"""
a=[1,2,3]
b=[1,2,3]
c=a
print(a is b)
print(a is c)
print(a is not b)

a=[1,2,3,4]
print(2 in a)
print(5 not in a)
print(100 is a)