# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, high, low):
            if not node:
                return True
            if not low < node.val < high:
                return False

            return valid(node.left, node.val, low) and valid(node.right, high,node.val)

        return valid(root, float("inf"), float("-inf"))