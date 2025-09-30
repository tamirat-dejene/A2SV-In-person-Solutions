# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        store = {}

        def dfs(nd):
            if not nd:
                return 0
            
            if nd not in store:
                store[nd] = max(dfs(nd.left) + dfs(nd.right), nd.val + (0 if not nd.left else dfs(nd.left.left) + dfs(nd.left.right)) + (0 if not nd.right else dfs(nd.right.left) + dfs(nd.right.right)))
            
            return store[nd]
        
        return dfs(root)
        