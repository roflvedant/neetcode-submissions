class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        res = []
        sub = []

        def dfs(i):
            if sum(sub) == target:
                res.append(sub.copy())
                return
            if i >= len(nums) or sum(sub) > target:
                return
            
            sub.append(nums[i])
            dfs(i)

            sub.pop()
            dfs(i+1)

        dfs(0)
        return res
