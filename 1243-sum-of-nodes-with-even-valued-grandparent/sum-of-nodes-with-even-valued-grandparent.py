# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(node, gp=-1):
            nonlocal res

            if gp == 0: res += node.val
            elif gp == 1 and node.val % 2 == 0:
                if node.left: res += node.left.val
                if node.right: res += node.right.val

            if node.left: dfs(node.left, 1 if node.val % 2 == 0 else gp - 1 if gp >= 0 else -1)
            if node.right: dfs(node.right, 1 if node.val % 2 == 0 else gp - 1 if gp >= 0 else -1)

        dfs(root)
        return res





        