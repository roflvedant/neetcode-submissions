class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[l] < nums[r] or l==r:
                return nums[l]
            elif nums[l] <= nums[m]:
                l = m + 1
            elif nums[r] > nums[m]:
                r = m

        return nums[m]