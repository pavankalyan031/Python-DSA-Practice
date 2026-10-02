num=13232
while num>0:
    last_digit=num%10
    #13232%10 gives 2
    print(last_digit, end="")
    num=num//10
    #gives the remaining number by removing last digit 