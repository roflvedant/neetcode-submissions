class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        MIN = nums[0]

        while l <= r:
            if nums[l] < nums[r]:
                return min(nums[l], MIN)

            m = (l+r) // 2
            MIN = min(MIN, nums[m])

            if nums[l] <= nums[m]:
                l = m + 1
            else:
                r = m - 1

        return MIN

