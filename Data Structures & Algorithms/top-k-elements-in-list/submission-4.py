class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        rank = [[] for i in range(len(nums)+1)]

        for i in nums:
            freq[i] = 1 + freq.get(i,0)
        for num, frq in freq.items():
            rank[frq].append(num)
        res= []
        for i in range(len(rank)-1, 0 , -1):
            for n in rank[i]:
                res.append(n)
                if len(res) == k:
                    return res
