class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        l = 0
        r = len(numbers) - 1

        res = []
        while l < r:
            add = numbers[l] + numbers[r]

            if add < target:
                l += 1
            elif add > target:
                r -= 1
            else:
                res.append(l+1)
                res.append(r+1)
                return res