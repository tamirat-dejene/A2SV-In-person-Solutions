# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int, p=None, d=2) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, root)
        if not p:
            p = root

        if d == depth:
            p.left = TreeNode(val, p.left)
            p.right = TreeNode(val, None, p.right)
            return root
        
        if p.left:
            self.addOneRow(root, val, depth, p.left, d + 1)
        if p.right:
            self.addOneRow(root, val, depth, p.right, d + 1)

        return root
        