class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []

        if nums[0] > 0:
            return []


        for i in range(len(nums)):
            
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            l = i + 1
            r = len(nums) - 1


            while l < r:
                add = nums[i] + nums[l] + nums[r]
                if add > 0:
                    r -= 1
                elif add < 0:
                    l += 1
                else:
                    res.append([nums[i] , nums[l] , nums[r]])
                    l += 1
                    r -= 1

                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                    while nums[r+1] == nums[r] and l < r:
                        r -= 1

        return res