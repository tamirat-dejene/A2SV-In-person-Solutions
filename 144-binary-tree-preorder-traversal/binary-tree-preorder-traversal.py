# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # res = []
        # def dfs_preo(node):
        #     if not node: return
        #     res.append(node.val)
        #     dfs_preo(node.left)
        #     dfs_preo(node.right)
        
        # dfs_preo(root)
        # return res

        stack, res = [root], []

        while stack:
            curr = stack.pop()
            if not curr: continue
            res.append(curr.val)
            stack.append(curr.right)
            stack.append(curr.left)
        
        return res