def maxprofit(prices):
    n= len(prices)
    min_price = prices[0]
    max_profit= 0

    for i in range(1, n):
        if prices[i]< min_price:
            min_price= prices[i]

        else:
            profit= prices[i] - min_price

            if profit> max_profit:
                max_profit= profit

    return max_profit


prices= [7,1,5,3,6,5]
print(maxprofit(prices))