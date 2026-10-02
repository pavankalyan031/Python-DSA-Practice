#sum of elements in a list  
"""

list= [1,2,3,4]
sum=0
for i in list:
    sum+=i #sum=sum+i
print(f"Sum of all elements in the list: {sum}")



#using function
def sum_of_all(list):
    sum=0
    for i in list:
        sum+=i
    return sum
list=[1,2,3,4]
# result= print(sum_of_all(list))
# print(f"sum of elements are: {result}")
print(sum_of_all(list))

"""