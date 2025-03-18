# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def equal(node1, node2):
            if not node1 and not node2: return True
            if not node1 or not node2 or node1.val != node2.val: return False

            return equal(node1.left, node2.left) and equal(node1.right, node2.right)
        
        def check(node, subtree):
            if not node: return False
            
            return (node.val == subtree.val and equal(node.left, subtree.left) and equal(node.right, subtree.right)) or check(node.left, subtree) or check(node.right, subtree)

        return check(root, subRoot)


            

        