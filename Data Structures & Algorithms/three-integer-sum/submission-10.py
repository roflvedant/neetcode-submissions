class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        
        
        #[-4,-1,-1,0,1,2]

        for i,n in enumerate(nums):

            if i > 0 and nums[i] == nums[i-1]:
                continue

            l = i + 1
            r = len(nums) - 1
            while l < r:
                sum = nums[l] + nums[r] + n
                if sum > 0:
                    r -= 1
                elif sum < 0:
                    l += 1
                else:
                    res.append([nums[l], nums[r], n])
                    l +=1
                    r -=1
                    while nums[l] == nums[l-1] and l <r:
                        l += 1
                    while nums[r] == nums[r+1] and l <r:
                        r -= 1
        return res



