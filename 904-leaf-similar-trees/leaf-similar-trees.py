# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def dfs(nd):
            if not nd:
                return []
            
            if not nd.left and not nd.right:
                return [nd.val]
            return dfs(nd.left) + dfs(nd.right)
        
        return dfs(root1) == dfs(root2)
        