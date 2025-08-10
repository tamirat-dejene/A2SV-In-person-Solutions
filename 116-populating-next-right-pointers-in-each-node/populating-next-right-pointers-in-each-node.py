"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        
        que = deque([root])

        while que:
            ln = len(que) # current level

            for i in range(ln):
                curr = que.popleft()
                curr.next = que[0] if i + 1 < ln else None

                if curr.left:
                    que.append(curr.left)
                if curr.right:
                    que.append(curr.right)

        return root

