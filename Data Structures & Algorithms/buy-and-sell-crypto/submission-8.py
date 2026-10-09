class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        MAX = 0
        l,r = 0, 1

        while r != len(prices):
            if prices[r] > prices[l]:
                MAX = max(MAX, prices[r] - prices[l])
            else:
                l=r
            r += 1
        return MAX
                         
    #prices=[5,-s-1,5,6,-e-7,0,10]