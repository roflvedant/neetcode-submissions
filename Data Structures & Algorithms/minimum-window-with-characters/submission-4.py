class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT = {}
        countS = {}


        for i in t:
            countT[i] = 1 + countT.get(i,0)

        have = 0
        need = len(countT)

        l = 0

        res = [-1,-1]

        resL = float("infinity")
        
        for r in range(len(s)):
            countS[s[r]] = 1 + countS.get(s[r], 0)

            if s[r] in countT and countT[s[r]] == countS[s[r]]:
                have += 1


            while have == need:
                if (r-l + 1) < resL:
                    res = [l,r]
                    resL = r-l+1

                countS[s[l]] -= 1

                if s[l] in countT and countS[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1

        l, r = res
        return s[l : r + 1] if resL != float("infinity") else "" 
