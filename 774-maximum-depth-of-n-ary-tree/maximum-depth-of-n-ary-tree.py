"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        vis = set([root])
        def dfs(nd):
            if not nd:
                return 0
            ans = 1
            for ch in nd.children:
                if ch not in vis:
                    vis.add(ch)
                    ans = max(1 + dfs(ch), ans)
            
            return ans
        
        return dfs(root)
        