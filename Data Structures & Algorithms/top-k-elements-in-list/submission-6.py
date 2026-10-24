class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frq = {}

        buck = [[] for n in range(len(nums) + 1)]

        res = []

        for i in nums:
            frq[i] = 1+ frq.get(i, 0)
        
        for val, count in frq.items():
            buck[count].append(val)
        
        for i in range(len(buck)-1, 0, -1):

            for num in buck[i]:
                res.append(num)
                k -= 1
                if k == 0:
                    return res