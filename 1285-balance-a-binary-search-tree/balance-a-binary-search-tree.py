# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        ordered = []
        def iot(node):
            if not node: return
            iot(node.left)
            ordered.append(node.val)
            iot(node.right)
        
        iot(root)

        def balanced(l, r):
            if l > r: return

            m =  ceil((l + r) / 2)

            node = TreeNode(ordered[m])
            node.left = balanced(l, m - 1)
            node.right = balanced(m + 1, r)

            return node
        
        return balanced(0, len(ordered) - 1)


        