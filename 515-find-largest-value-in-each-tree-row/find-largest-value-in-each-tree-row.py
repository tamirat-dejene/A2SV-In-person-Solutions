# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        lvl = {}

        def dfs(node, l=1):
            if not node: return
            
            lvl[l] = max(node.val, lvl.get(l, node.val))
            if node.left: dfs(node.left, l + 1)
            if node.right: dfs(node.right, l + 1)
        
        dfs(root)
        
        return [lvl[i] for i in range(1, len(lvl) + 1)]


        