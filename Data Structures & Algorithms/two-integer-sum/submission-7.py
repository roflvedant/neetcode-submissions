class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = {}
        for i in range(0, len(nums)):
            golden = target - nums[i]
            if golden in prev:
                return [prev[golden], i]
            prev[nums[i]] = i



        
