# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        ans = 0
        def dfs(node, rsum=0, hmap={0:1}):
            nonlocal ans, targetSum
            if not node: return
            rsum += node.val

            if rsum - targetSum in hmap:
                ans += hmap[rsum - targetSum]
            
            hmap[rsum] = hmap.get(rsum, 0) + 1

            dfs(node.left, rsum, hmap.copy())
            dfs(node.right, rsum, hmap.copy())
        
        dfs(root)

        return ans