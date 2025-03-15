# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        
        queue = deque([(root, 1)])

        ans = defaultdict(deque)

        # bfs
        while queue:
            node, lvl = queue.popleft()
            if lvl % 2 == 0:
                ans[lvl].appendleft(node.val)
            else: ans[lvl].append(node.val)

            if node.left: queue.append((node.left, lvl + 1))
            if node.right: queue.append((node.right, lvl + 1))

        return [list(ans[lv]) for lv in range(1, len(ans) + 1)]




        