# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = float('-inf')

        def dfs(node):
            nonlocal ans

            if not node or (not node.left and not node.right):
                return float('-inf') if not node else node.val
            
            lft = dfs(node.left)
            rgt = dfs(node.right)

            mx = max(lft, rgt)

            ans = max(
                node.val + lft + rgt, 
                lft + node.val, 
                rgt + node.val,
                lft,
                rgt,
                ans
            )

            return max(mx + node.val, node.val)

        
        ans = max(dfs(root), ans)

        return ans
            
