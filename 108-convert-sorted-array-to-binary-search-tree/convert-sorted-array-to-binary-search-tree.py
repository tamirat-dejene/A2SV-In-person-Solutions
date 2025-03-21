# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def build(l, r):
            if l > r: return None
            m = ceil((l + r) / 2)
            
            node = TreeNode(nums[m])

            node.left = build(l, m - 1)
            node.right = build(m + 1, r)

            return node

        return build(0, len(nums) - 1)