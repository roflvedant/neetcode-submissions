class Solution:
    def maxArea(self, h: List[int]) -> int:
        l = 0
        r = len(h) - 1

        MAX = 0

        while l < r:
            area = (r-l) * min(h[l],h[r])

            if h[l] < h[r]:
                l += 1
            else:
                r -= 1
            
            MAX = max(MAX, area)
        
        return MAX