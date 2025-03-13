# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # res = []
        # def dfs_poso(node):
        #     if not node: return
        #     dfs_poso(node.left)
        #     dfs_poso(node.right)
        #     res.append(node.val)
        # return dfs_poso(root)

        stack, visited, res = [root], set(), []
        if not root: return res

        while stack:
            curr = stack[-1]

            # right subtree
            if curr.right and curr.right not in visited:
                stack.append(curr.right)
                if not curr.left: continue
            
            # left subtree
            if curr.left and curr.left not in visited:
                stack.append(curr.left)
                continue

            # root
            curr = stack.pop()
            visited.add(curr)
            res.append(curr.val)
                
                    
        return res
            