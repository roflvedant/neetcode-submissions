class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        hashset = set()

        l,r = 0,0

        MAX = 0

        for r in range(len(s)):
            while s[r] in hashset:
                hashset.remove(s[l])
                l += 1
            
            hashset.add(s[r])
            MAX = max(r-l+1, MAX)

        return MAX