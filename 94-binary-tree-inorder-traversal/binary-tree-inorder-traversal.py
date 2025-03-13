# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # def dfs_it(node, res=[]):
        #     if not node: return res
        #     dfs_it(node.left, res)
        #     res.append(node.val)
        #     dfs_it(node.right, res)

        #     return res
        # return dfs_it(root)

        stack, visited, res = [root], set(), []
        if not root: return res

        while stack:
            curr = stack.pop()

            # left subtree
            if curr.left and curr.left not in visited:
                stack.append(curr)
                stack.append(curr.left) # access the left first
                continue
            
            # we are here means, we visited left subtree. then we need to visit the root, and push the right subtree to the stack
            if curr.right and curr.right not in visited:
                stack.append(curr.right)
            
            res.append(curr.val)
            visited.add(curr)
            
        return res
