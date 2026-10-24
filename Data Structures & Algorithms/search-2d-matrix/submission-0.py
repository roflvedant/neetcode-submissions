class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        l = 0
        r = len(matrix[0]) - 1

        L = 0 
        R = len(matrix) - 1
        while L <= R:
            

            row = (L+R) // 2

            if matrix[row][0] <= target <= matrix[row][len(matrix[0]) - 1]:
                
                while l <= r:
                    m = (l+r) // 2
                    
                    if matrix[row][m] == target:
                        return True
                    elif matrix[row][m] <= target:
                        l = m + 1
                    else:
                        r = m - 1
                return False
            
            elif target < matrix[row][0]:
                R = row - 1
            elif target >= matrix[row][len(matrix[0]) - 1] or L == R:
                L = row + 1
        
        return False