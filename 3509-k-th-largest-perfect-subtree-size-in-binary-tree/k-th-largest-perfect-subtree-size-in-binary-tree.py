# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:
        keep = []

        def dfs(nd): # node count, depth
            if not nd: 
                return 0, 0

            lftc, dl = dfs(nd.left)
            rgtc, dr = dfs(nd.right)

            tot = lftc + rgtc + 1
            d = max(dl, dr) + 1

            pc = 2**d - 1
            if pc == tot:
                keep.append(pc)
            
            return tot, d
        dfs(root)
        keep.sort(reverse=True)

        if k > len(keep):
            return -1
        return keep[k-1]

