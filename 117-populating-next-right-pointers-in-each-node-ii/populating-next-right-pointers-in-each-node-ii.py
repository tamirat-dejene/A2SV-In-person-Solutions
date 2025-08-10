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
            ln, prev = len(que), None
            
            for _ in range(ln):
                curr = que.popleft()
                if not curr: continue

                if not prev:
                    prev = curr
                else:
                    prev.next = curr
                    prev = curr

                if curr.left:
                    que.append(curr.left)
                else:
                    que.append(None)

                if curr.right:
                    que.append(curr.right)
                else:
                    que.append(None)

        return root

