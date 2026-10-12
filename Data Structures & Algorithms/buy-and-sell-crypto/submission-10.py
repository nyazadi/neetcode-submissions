class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = ans = curr = 0 

        for r in range(len(prices)): 
            curr = prices[r] - prices[left]
            ans = max(ans,curr)
            while prices[r]<prices[left]:
                left+=1
        return ans 


        