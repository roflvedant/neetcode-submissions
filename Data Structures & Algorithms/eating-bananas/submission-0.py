class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        maxP = 0
        for n in piles:
            maxP = max(n,maxP)
        
       
        l = 1
        r = maxP

        minK = float("infinity")

        while l <= r:

            m = (l+r) // 2
            oneRound = 0
            for plate in piles:
                oneRound += math.ceil(plate/m)
            
            if oneRound <= h:
                minK = min(minK, m)
                r = m - 1
            else:
                l = m + 1

        return minK if minK != float("infinity") else maxP
            