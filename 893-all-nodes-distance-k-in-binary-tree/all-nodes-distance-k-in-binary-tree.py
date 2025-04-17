# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(set)
        stack = [root]

        while stack:
            curr = stack.pop()

            if curr.right:
                graph[curr.val].add(curr.right.val)
                graph[curr.right.val].add(curr.val)
                stack.append(curr.right)
            if curr.left:
                graph[curr.val].add(curr.left.val)
                graph[curr.left.val].add(curr.val)
                stack.append(curr.left)
        
        
        queue = deque([(target.val, 0)])
        visited = set([target.val])
        res = []
        
        while queue:
            node, dpth = queue.popleft()

            if dpth == k:
                res.append(node)
            
            for ne in graph[node]:
                if ne not in visited:
                    visited.add(ne)
                    queue.append((ne, dpth + 1))
        
        return res


        
