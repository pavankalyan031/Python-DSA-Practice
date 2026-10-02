#using while loop means iteration method

s=input("Enter a string to check: ")
left=0
right=len(s)-1
while left<right:
    if s[left]!=s[right]:
        print("Not Pal")
        break
    left+=1
    right-=1

else:
    print("Pal")
    
    
#using function
def is_pal(s):
    left=0
    right=len(s)-1
    
    while left<right:
        if s[left]!=s[right]:
            return False
        
        left+=1
        right-=1
    return True

s=input("Enter a string to check: ")
print(is_pal(s))



#using recursion:
def is_palindrom(text, left, right):
    