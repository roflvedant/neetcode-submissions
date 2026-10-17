class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dic = defaultdict(list)

        for word in strs:
            frq = [0]*26
            for letter in word:
                frq[ord(letter) - ord('a')] += 1
            dic[tuple(frq)].append(word)

        return list(dic.values())

        
                