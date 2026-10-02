"""
while loop:
1. while loop
"""
a="pavan"
i=0
while i< len(a):
    print(a[i])
    i+=1


print()

#2. continue statement
a="pavan"
i=0
while i< len(a):
    if a[i]=="a" or a[i] == 'v':
        i+=1
        continue
    print(a[i])
    i+=1
    
print()
 
# 3. break statement
a="Pavan"
i=0
while i<len(a):
    if a[i]=='a':
        i+=1
        break
    print(a[i])
    i+=1
    
print()
   
#4. pass statement
a="pavan"
i=0
while i<len(a):
    i+=1
    pass
print(i)