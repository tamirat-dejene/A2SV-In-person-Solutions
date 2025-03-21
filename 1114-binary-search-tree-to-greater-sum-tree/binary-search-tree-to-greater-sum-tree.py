# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        sm = 0
        def trav(node):
            nonlocal sm
            if not node: return 0

            trav(node.right)
            sm += node.val
            node.val = sm
            trav(node.left)

            return node.val
      
        trav(root)

        return root