# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = deque([root])
        ans = []

        while queue:
            sm, ln = 0, len(queue)

            for i in range(ln):
                nd = queue.popleft()
                sm += nd.val

                if nd.left:
                    queue.append(nd.left)
                if nd.right:
                    queue.append(nd.right)
                
            ans.append(sm / ln)
        
        return ans
        