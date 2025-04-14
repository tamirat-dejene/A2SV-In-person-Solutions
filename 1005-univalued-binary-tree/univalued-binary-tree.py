# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        queue = [root]
        v = root.val
        while queue:
            nd = queue.pop()
            if nd.val != v: return False
            if nd.left: queue.append(nd.left)
            if nd.right: queue.append(nd.right)
        
        return True
            





        