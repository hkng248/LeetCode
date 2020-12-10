class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = float('inf') 
        maxProfit = 0 
        for stock in prices:
            if stock < minPrice:
                minPrice = stock 
            elif(stock - minPrice > maxProfit):
                maxProfit = stock - minPrice 
        return maxProfit 
        