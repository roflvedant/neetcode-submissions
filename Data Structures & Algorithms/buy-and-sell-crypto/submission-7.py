class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        MAX= 0
        l = 0

        for r in range(len(prices)):
            if r == 0:
                r +=1
            else: 
                prof = prices[r] - prices[l]
                if prof > 0:
                    MAX = max(MAX, prof)
                else:
                    l = r
        return MAX
             
    #prices=[5,-s-1,5,6,-e-7,0,10]