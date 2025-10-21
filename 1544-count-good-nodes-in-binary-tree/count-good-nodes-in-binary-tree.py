# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(nd, mx):
            if not nd:
                return 0

            return (1 if nd.val >= mx else 0) + dfs(nd.left, max(nd.val, mx)) + dfs(nd.right, max(nd.val, mx))
        
        return dfs(root, -inf)
        