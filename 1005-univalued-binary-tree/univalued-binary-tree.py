# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        def bfs(node):
            if not node: return True

            if (not node.left  or node.left.val == node.val) and (not node.right or node.right.val == node.val):
                return bfs(node.left) and bfs(node.right)
            return False
        
        return bfs(root)

        