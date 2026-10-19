class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        r = max(piles)
        l = 1
        ans = float("inf")
        while l <= r:

            m = (l+r) // 2

            res = 0
            for n in piles:
                res += math.ceil(n/m)
            
            if res <= h:
                ans = min(m, ans)
                r = m - 1
            else:
                l = m + 1

        return ans 