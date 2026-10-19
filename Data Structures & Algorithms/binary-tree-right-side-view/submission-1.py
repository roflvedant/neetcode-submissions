# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        #BFS

        window = []

        q = deque([root])

        while q:
            rightSide = None
            for i in range(len(q)):
                val = q.popleft()
                if val:
                    rightSide = val

                    q.append(val.left)
                    q.append(val.right)
            if rightSide:
                window.append(rightSide.val)
        return window
                        

     
            