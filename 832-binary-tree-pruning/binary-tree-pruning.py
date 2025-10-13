# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(nd):
            if not nd:
                return 0, None
            
            lc, _ = dfs(nd.left)
            rc, _ = dfs(nd.right)

            res = nd.val
            
            if lc == 0:
                nd.left = None
            else:
                res += lc
            
            if rc == 0:
                nd.right = None
            else:
                res += rc
            
            if res == 0:
                nd = None

            return res, nd
        
        return dfs(root)[1]