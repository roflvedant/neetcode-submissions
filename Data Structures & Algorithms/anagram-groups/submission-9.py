class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = defaultdict(list)
        for n in range(len(strs)):
            frq = [0]*26   
            for i in strs[n]:
                frq[ord(i)- ord('a')] += 1
            dict[tuple(frq)].append(strs[n])
        return list(dict.values())
                
        