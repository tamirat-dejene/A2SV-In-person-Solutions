# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(node, dpth):

            l_dca, ld = dfs(node.left, dpth + 1) if node.left else (node, dpth)
            r_dca, rd = dfs(node.right, dpth + 1) if node.right else (node, dpth)

            if ld == rd:
                return (node, ld)

            if ld > rd:
                return (l_dca, ld)
            
            return (r_dca, rd)
        
        return dfs(root, 0)[0]
        