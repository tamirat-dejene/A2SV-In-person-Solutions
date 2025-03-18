# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def preorder(curr):
            if not curr: return []

            if not curr.left and not curr.right: return [[str(curr.val)]]

            left = preorder(curr.left) if curr.left else []
            right = preorder(curr.right) if curr.right else []

            for i in range(len(left)):
                left[i] = [str(curr.val)] + left[i]
            
            for i in range(len(right)):
                right[i] = [str(curr.val)] + right[i]
            
            return left + right
        
        return sum(int(''.join(num)) for num in preorder(root))