""" 
given an array of a week's stock prices, return the maximum profit achiveable by buying and selling at different days
for example: 
Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
                Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
                Sum the two -> 7
"""

def max_profit(prices: list) -> int:
    return sum( diff for i in range(len(prices) - 1) if (diff := prices[i + 1] - prices[i]) > 0 )


if __name__ == "__main__":
    tests = [[1,2,3,4,5], [7,1,5,3,6,4], [7,6,4,3,1] ]
    for test in tests:
        print(f'for {test} \tmax --> {max_profit(test)}')