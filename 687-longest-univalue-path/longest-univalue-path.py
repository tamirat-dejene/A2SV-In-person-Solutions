# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(node):
            nonlocal ans

            if not node: return -1, None

            cl, vl = dfs(node.left)
            cr, vr = dfs(node.right)

            ans = max(
                ans,
                cl + (1 if vl == node.val else 0),
                cr + (1 if vr == node.val else 0),
                (cl + cr + 2) if vl == vr == node.val else 0
            )

            if vl == vr == node.val: return max(cl, cr) + 1, node.val
            if vl == node.val: return cl + 1, node.val
            if vr == node.val: return cr + 1, node.val

            return 0, node.val



        dfs(root)

        return ans

            


            
