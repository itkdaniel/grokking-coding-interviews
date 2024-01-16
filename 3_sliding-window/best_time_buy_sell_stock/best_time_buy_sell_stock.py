# vim: set comments=sb\:\"\"\",mb\:##\ \ \ ,ex-3\:\"\"\",fb\:\*,fb\:-,\:##:
# vim: set fo=tcq1rowpn:

##   Best Time to Buy and Sell Stock
##
##   Problem Statement
"""
##   Given an array where the element at the index i represents the price of 
##   a stock on day i, find the maximum profit that you can gain by buying the 
##   stock once and then selling it.
##
##   **Note**: You can buy the stock on once specific day and sell it on 
##   a different day to make profit. If no profit can be achieved, we return 0.
##
##   Constraints:
##   * We cant sell before buying a stock, that is the array index at whieh 
##     stock is bought will always be less than the index at which the stock is 
##     sold
##   * 1 <= prices.length <= 10^3
##   * 0 <= prices[i] <= 10^5
##
##   Example 1:
##   Input: prices = [7,1,5,3,6,4]
##   Output: 5
##
##   Example 2:
##   Input: prices = [10,8,6,4,2]
##   Output: 0
##   
"""
##   Understand the Problem
"""
##   1. What should be the output if the following prices are given as an input?
##   Input: prices = [10,4,11,1,5]
##   :: Output: 7
##
##   2. What should be the output if the following prices are given as an input?
##   Input: prices = [7,7,6,6,6]
##   :: Output: 0
##
##   3. What should be the output if the following prices are given as an input?
##   Input: prices = [4,10,5,1,6,7]
##   :: Output: 6
##
##   4. What should be the output if the following prices are given as an input?
##   Input: prices = [4,4,4,3,3,4]
##   :: Output: 1
##
"""
##   Arrange the Steps
"""
##                      s
##   [1,2,4,2,5,7,2,4,9,0,9]
##    0 1 2 3 4 5 6 7 8 9 0                
##                        e
##    s,e = 9,10
##    cp = 9
##    mp = 9
##    mn = 9
##    mx = 10
##
##   1. Initialize the start and end indexes to be 0.
##   2. Initialize variables to hold the current and max profit values.
##   3. Initialize variables to hold the index of minimum and maximum values for 
##      the current window.
##   4. Iterate the entire list incrementing the end index until reaching the 
##      end of the array.
##   5. In each iteration update the current profit, min and max values accordingly. 
##   6. If value at current index is greater than the value at start index and 
##      greater than current max, update the current and max profit.
##   7. If the value at current index is less than the current min value, set 
##      start to the current index and update the current min value.
##   8. Return the max profit if max profit is not equal to -inf else 0.
##
"""
##   Write the Solution Code
def max_profit(prices: list[int])->int:
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        max_profit = max(price-min_price, max_profit)
    return f'{ min_price=},\n\t  {max_profit=}\n',max_profit

##   Solution Summary
"""
##   The sliding window is applied in the above solution. It maintains a moving 
##   subset of elements (i.e min_price and max_profit) to process the sequential 
##   data (prices).
##   The code follows proper language guidelines and uses meaningful variable 
##   names and follows indentation and spacing conventions, as well as includes 
##   comments to explain the logic.
##   Overall, the code looks good and efficiently finds the masimum profit that 
##   can be obtained by buying and selling a stock based on its prices on 
##   different days.
##
"""
##   Time Complexity
"""
##   The time complexity of the solution is O(n), where n is the length of the 
##   input list, prices. This is because we iterate through the list at most 
##   once using a single loop and perform constant time operations for each 
##   element. The built-in Python functions, such as 'float' and 'max', also 
##   have constant time complexity.
##
"""
##   Space Complexity
"""
##   The space complexity of the above solution is O(1) because it only uses 
##   a cconstant amount of extra space to store the minimum price and maximum 
##   profit variables. The space complexity of the built-in Python functions 
##   used in the code, such as float() and max(), are also O(1) since they do 
##   not require any additional space that grows with the input size.
##
"""

def max_profit1(prices: list[int])->int:
    min_price = 0
    current_profit = 0
    max_profit = 0
    for current_price in range(1,len(prices)):
        current_profit = prices[current_price] - prices[min_price]
        if prices[current_price] < prices[min_price]:
            min_price = current_price
        else:
            max_profit = max(current_profit,max_profit)
    return f'{ min_price=},\n\t  {current_profit=},\n\t  {max_profit=}\n',max_profit

def max_profit2(prices: list[int])->int:
    """
      s
##   [1,2,4,2,5,7,2,4,9,0,9]
##    0 1 2 3 4 5 6 7 8 9 0
##          e
##    s,e = 9,10
##    cp = 9
##    mp = 9
##    mn = 9
##    mx = 10
##
"""
    start = 0
    current_min = 0
    current_max = 0
    current_profit = 0
    max_profit = 0
    for index,value in enumerate(prices):
        # current index is greater than the start index
        if index > start:
            # current value is >= start value
            if prices[index] >= prices[start]:
                # current value is >= current max value
                if prices[index] >= prices[current_max]:
                    current_max = index
            else: # current value is less than start value
                current_min = index
                start = current_min
            current_profit = prices[index]-prices[start]
        max_profit = max(current_profit,max_profit)
    return f'{ current_min=},\n\t  {current_max=},\n\t  {current_profit=},\n\t  {max_profit=}\n',max_profit
