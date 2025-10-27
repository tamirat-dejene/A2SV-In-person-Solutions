class Solution:
    def diameter(self, tree):
        def dfs(start):
            stack = [(start, 0)]
            vis = set([start])
            ans = (0, start)

            while stack:
                curr, dis = stack.pop()
                ans = max(ans, (dis, curr))

                for ne in tree[curr]:
                    if ne not in vis:
                        vis.add(ne)
                        stack.append((ne, dis + 1))
            
            return ans
        
        _, f = dfs(0) # find farthest from an arbitrary node
        
        return dfs(f)[0] # find the farthest again

    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        tree1 = [[] for _ in range(len(edges1) + 1)]
        tree2 = [[] for _ in range(len(edges2) + 1)]

        for a, b in edges1:
            tree1[a].append(b)
            tree1[b].append(a)
        
        for a, b in edges2:
            tree2[a].append(b)
            tree2[b].append(a)

        d1 = self.diameter(tree1)
        d2 = self.diameter(tree2)

        return max(d1, d2, math.ceil(d1 / 2) + math.ceil(d2 / 2) + 1)

        