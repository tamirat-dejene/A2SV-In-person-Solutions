# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        def dfs(node, mn, mx):
            if not node: return abs(mx - mn)

            lft = dfs(node.left, min(mn, node.val), max(mx, node.val))
            rgt = dfs(node.right, min(mn, node.val), max(mx, node.val))

            return max(lft, rgt)
        
        return dfs(root, root.val, root.val)