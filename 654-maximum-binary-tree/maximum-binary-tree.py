# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
    
        def dfs(l, r):
            if l > r: return None

            m = nums.index(max(nums[l:r+1]))
            node = TreeNode(nums[m])
            node.left = dfs(l, m - 1)
            node.right = dfs(m + 1, r)

            return node
        
        return dfs(0, len(nums) - 1)


    
        