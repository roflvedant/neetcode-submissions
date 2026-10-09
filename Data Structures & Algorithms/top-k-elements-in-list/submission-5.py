class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        buck = [[] for i in range(len(nums) + 1)]
        res = []

        for n in nums:
            freq[n] = 1 + freq.get(n, 0)
        
        for val, frq in freq.items():
            buck[frq].append(val)

        for i in range(len(buck)-1,0,-1):
            for n in buck[i]:
                res.append(n)
                if len(res) == k:
                    return res