"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in
 the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0
        i = 0
        for j in range(1, len(prices)):
            if prices[i] < prices[j]:
                s = prices[j] - prices[i]
                max_profit = max(max_profit, s)
            else:
                i = j

            j = j + 1
        return max_profit

    """
    - set Initial maximum profit as zero
    
    - Initialize two pointers 'i = 0' and 'j = 1' where, 'i' represents the day you buy stock and 'j' 
      represents the day you sell stock
      
    - If the price at day 'j' is greater than at day 'i', then it is a profit. calculate the profit and 
      store the maximum value in 'max_profit'.
      
    - If the price at day 'j' is lesser than at day 'i', then make sure to move the pointer 'i' to where
      the pointer 'j' was present. The stock should be bought on the day when it is at the lowest price.
      
    - increment the pointer 'j' until iterates throughout the array. 
    
    - return the maximum profit 'max_profit'.
    """