# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(node1, node2):
            node2.val += node1.val

            if node1.left and node2.left:
                dfs(node1.left, node2.left)
            elif node1.left:
                node2.left = node1.left
            
            if node1.right and node2.right:
                dfs(node1.right, node2.right)
            elif node1.right:
                node2.right = node1.right
        
        if not root1 or not root2: return root1 if root1 else root2
        
        dfs(root1, root2)

        return root2