class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        l, r = 0, len(height) - 1
        LMAX = height[l]
        RMAX = height[r]

        res = 0

        while l < r:
            
            if LMAX < RMAX:
                l += 1
                LMAX = max(LMAX, height[l])
                res += (LMAX - height[l])
            else: 
                r -= 1
                RMAX = max(RMAX, height[r])
                res += (RMAX - height[r])
        return res