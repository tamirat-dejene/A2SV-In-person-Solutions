class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        tree = [set() for _ in range(n)]
        deg = [0] * n

        for r, c in edges:
            tree[r].add(c)
            tree[c].add(r)
            deg[c] += 1
            deg[r] += 1

        queue = deque([nd for nd in range(n) if deg[nd] == 1 or deg[nd] == 0])
        ans = list(queue)
        vis = set(queue)

        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()

                for ne in tree[curr]:
                    if ne not in vis:
                        deg[ne] -= 1

                        if deg[ne] == 1:
                            vis.add(ne)
                            queue.append(ne)
            if not queue:
                return ans
            ans = list(queue)

        return ans