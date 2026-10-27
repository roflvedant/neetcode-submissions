class Solution:
    def maxProfit(self, p: List[int]) -> int:
        MAX = 0

        l = 0

        for r in range(1, len(p)):
            prof = p[r] - p[l]
            if prof < 0:
                l = r
            MAX = max(prof, MAX)

        return MAX

    #prices=[5,-s-1,5,6,-e-7,0,10]