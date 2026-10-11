class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = {}

        for i in range(len(nums)):
            match = target - nums[i]
            if match in prev:
                return([prev[match], i])
            else:
                prev[nums[i]] = i
            





        
