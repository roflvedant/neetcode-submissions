class Solution:
    def trap(self, h: List[int]) -> int:

        l = 0
        r = len(h) - 1 
        
        LMAX = h[l] # 2 , 
        RMAX = h[r] # 1 , 2 , 3 

        res = 0

        while l < r:
            
            if LMAX < RMAX:
                l += 1
                LMAX = max(LMAX, h[l])

                res += LMAX - h[l]
            else:
                r -= 1

                RMAX = max(RMAX, h[r])

                res += RMAX - h[r]

        return res 


       