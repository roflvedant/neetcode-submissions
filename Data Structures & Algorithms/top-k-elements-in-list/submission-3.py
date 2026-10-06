class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            freq[i] = 1 + freq.get(i,0)
            # 1 -> 1; 2-> 2, 3 -> 3
        rank = [[] for i in range(len(nums) + 1)]
        for key, value in freq.items():
            rank[value].append(key)
        
        res = []
        for i in range(len(rank)-1, 0, -1):
            for n in rank[i]:
                res.append(n)
                if len(res) == k:
                    return res