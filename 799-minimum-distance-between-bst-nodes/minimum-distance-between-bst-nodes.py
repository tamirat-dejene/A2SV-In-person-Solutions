# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        
        stack, vis = [root], set()
        ans, prev = inf, -1

        while stack:
            nd = stack[-1]

            if nd.left and nd.left not in vis:
                stack.append(nd.left)
            else:
                if prev != -1:
                    ans = min(ans, nd.val - prev)
                
                prev = stack.pop().val
                vis.add(nd)
                
                if nd.right and nd.right not in vis:
                    stack.append(nd.right)
        
        return ans


