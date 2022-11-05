class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxp = 0
        
        minp = prices[0]
        
        for i in range(1,len(prices)):
            maxp = max(prices[i]- minp,maxp)
            minp = min(minp, prices[i])
        
        return maxp
        