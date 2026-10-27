class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

    
        frq1 = [0]*26
        frq2 = [0]*26

        l = 0

        for r in range(len(s1)):

            frq1[ord(s1[r]) - ord('a')] += 1
            frq2[ord(s2[r]) - ord('a')] += 1   

        if frq1 == frq2:
            return True

        
        for r in range(len(s1),len(s2)):
            frq2[ord(s2[r]) - ord('a')] += 1
            frq2[ord(s2[l]) - ord('a')] -= 1
            l += 1


            if frq1 == frq2:
                return True
        
        return False