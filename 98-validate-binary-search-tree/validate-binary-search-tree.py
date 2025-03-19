# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node, mn=float('-inf'), mx=float('inf')):
            if not node: return True

            if node.val <= mn or node.val >= mx: return False

            return dfs(node.left, mn, node.val) and dfs(node.right, node.val, mx)

        return dfs(root)
        