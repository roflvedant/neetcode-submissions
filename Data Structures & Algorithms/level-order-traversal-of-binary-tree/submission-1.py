# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
       
        q = deque([root])
        res = []


        while q:
            window = []
            for i in range(len(q)):
                
                val = q.popleft()
                if val:
                    window.append(val.val)            
                    q.append(val.left)
                    q.append(val.right)

            if window:
                res.append(window) 

        return res