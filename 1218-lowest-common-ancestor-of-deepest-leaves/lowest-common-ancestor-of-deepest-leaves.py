# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = [(root, 0)]
        deepest = [0, [root]]
        parent = {root:root}

        while stack:
            node, dpth = stack.pop()

            if dpth > deepest[0]:
                deepest = [dpth, [node]]
            elif dpth == deepest[0]:
                deepest[1].append(node)

            if node.left:
                stack.append((node.left, dpth + 1))
                parent[node.left] = node

            if node.right:
                stack.append((node.right, dpth + 1))
                parent[node.right] = node
        
        while True:
            par = set()

            if len(deepest[1]) == 1:
                return list(deepest[1])[0]

            for dp in deepest[1]:
                par.add(parent[dp])

            deepest[1] = par

        return root
