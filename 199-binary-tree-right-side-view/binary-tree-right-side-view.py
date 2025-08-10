# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []

        q = deque([root])
        res = []

        while q:
            k = None

            for _ in range(len(q)):
                curr = q.popleft()
                if not curr: continue
                k = curr
                q.append(curr.left)
                q.append(curr.right)
            
            if k:
                res.append(k.val)
        
        return res