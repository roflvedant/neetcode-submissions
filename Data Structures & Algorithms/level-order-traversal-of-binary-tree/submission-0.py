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
            wnd = []
            for i in range(len(q)):
                val = q.popleft()
                if val:
                    wnd.append(val.val)
                    if val.left:
                        q.append(val.left)
                    if val.right:
                        q.append(val.right)
            if wnd:
                res.append(wnd)
        return res