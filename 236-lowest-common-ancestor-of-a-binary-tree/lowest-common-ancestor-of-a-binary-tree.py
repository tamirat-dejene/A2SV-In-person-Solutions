# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # DFS
        def dfs(nd, find, path):
            if nd == find:
                return path

            if nd.left:
                path.append(nd.left)
                lp = dfs(nd.left, find, path)

                if lp:
                    return lp

            if nd.right:
                path.append(nd.right)
                rp = dfs(nd.right, find, path)
                
                if rp:
                    return rp
            
            if path: path.pop()
            return []
        
        pp = dfs(root, p, [root])
        pq = dfs(root, q, [root])

        res = root
        for i in range(min(len(pp), len(pq))):
            if pp[i] == pq[i]:
                res = pp[i]
                continue
            break                

        return res

            
                    
