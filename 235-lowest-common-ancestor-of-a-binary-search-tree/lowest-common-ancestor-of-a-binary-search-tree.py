# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(curr, node1, node2):
            if not node1 or not node2: return curr

            if node1.val == curr.val or node2.val == curr.val or node1.val < curr.val < node2.val or node2.val < curr.val < node1.val: return curr

            if node1.val < curr.val:
                return dfs(curr.left, node1, node2)
            else:
                return dfs(curr.right, node1, node2)
        
        return dfs(root, p, q)
            
        