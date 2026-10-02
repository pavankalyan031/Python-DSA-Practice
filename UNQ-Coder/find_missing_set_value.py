def find_missing_value(set_a):
    
    n=len(set_a)+1
    expected_sum= n*(n+1)//2
    actual_sum = sum(set_a)
    missing_value= expected_sum-actual_sum
    return missing_value

set_a={1,2,3,4,6}
print(find_missing_value(set_a))


#aproach 2 using for loop
set_1={1,2,3,5,6}
n=len(set_1)+1
for i in range(1, n+1):
    if i not in set_a:
        print(f"missing value is : {i}")
        break