class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l, r = 0, 0
        hashset = set()
        MAX = 0

        while r != len(s):
            if s[r] not in hashset:
                hashset.add(s[r])
                MAX = max(MAX, r-l+1)
                r +=1
            else:
                hashset.remove(s[l])
                l += 1
        return MAX


#[ z, --x, y, z, --y, y, z   ]     set = { y }