# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0 
        def dfs(nd):
            nonlocal ans
            if not nd.left and not nd.right:
                return 1
            lft = dfs(nd.left) if nd.left else 0
            rgt = dfs(nd.right) if nd.right else 0

            ans = max(ans, lft + rgt)

            return max(lft, rgt) + 1
        dfs(root)
        return ans