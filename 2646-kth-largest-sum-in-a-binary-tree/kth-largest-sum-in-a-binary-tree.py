# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        queue = deque([(root, 1)])
        lsum = defaultdict(int)

        while queue:
            nd, lvl = queue.popleft()
            lsum[lvl] += nd.val

            if nd.left:
                queue.append((nd.left, lvl + 1))
            
            if nd.right:
                queue.append((nd.right, lvl + 1))

        if k > len(lsum):
            return -1
            
        return sorted(lsum.values(), reverse=True)[k - 1]