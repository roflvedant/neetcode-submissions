class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        frq = {}

        l = 0

        MAX = 0

        for r in range(len(s)):

            frq[s[r]] = 1 + frq.get(s[r], 0)

            while (r-l+1) - max(frq.values()) > k:                
                frq[s[l]] -= 1
                l += 1

            MAX = max(MAX, r-l+1)

        return MAX