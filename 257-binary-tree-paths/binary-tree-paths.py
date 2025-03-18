# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        def dfs(node):
            # leaf
            if not node.left and not node.right: return [[str(node.val)]]

            left = [] if not node.left else dfs(node.left)
            righ = [] if not node.right else dfs(node.right)

            left = [[str(node.val)] + l for l in left]
            righ = [[str(node.val)] + r for r in righ]

            return left + righ
        
        return ['->'.join(path) for path in dfs(root)]