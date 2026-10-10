class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        frq2 = [0]*26
        wSize = len(s1)
        
        for i in range(len(s1)):
            frq2[ord('a')-ord(s1[i])] += 1

        l = 0
        r = wSize - 1

        while r != len(s2):
            frq1 = [0]*26
            for i in range(l, r+1):
                frq1[ord('a')-ord(s2[i])] += 1
            if frq1 == frq2:
                return True
            l += 1
            r += 1
        return False
        