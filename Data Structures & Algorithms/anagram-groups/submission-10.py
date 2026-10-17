class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dic = defaultdict(list)

        for word in strs:
            freq = [0]*26
            for letter in word:
                freq[ord(letter) - ord('a')] += 1
            dic[tuple(freq)].append(word)

        return list(dic.values())
        
                