# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        # Visit inorder
        stack, store, vis = [root], [], set()
        while stack:
            tp = stack[-1]

            if tp.left and tp.left not in vis:
                stack.append(tp.left)
                vis.add(tp.left)
            else:
                store.append(stack.pop().val)
                if tp.right and tp.right not in vis:
                    stack.append(tp.right)
                    vis.add(tp.right)

        # Update inorder
        stack, vis = [root], set()
        store.sort() # sort
        i = 0

        while stack:
            tp = stack[-1]

            if tp.left and tp.left not in vis:
                stack.append(tp.left)
                vis.add(tp.left)
            else:
                stack.pop().val, i = store[i], i + 1
                if tp.right and tp.right not in vis:
                    stack.append(tp.right)
                    vis.add(tp.right)
