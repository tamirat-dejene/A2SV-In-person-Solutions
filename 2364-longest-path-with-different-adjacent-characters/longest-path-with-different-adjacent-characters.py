class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        tree = defaultdict(list)
        for i in range(1, len(s)):
            tree[i].append(parent[i])
            tree[parent[i]].append(i)

        ans = 1
        visited = set([0])

        def dfs(nd):
            nonlocal ans
            # check leaf
            if len(tree[nd]) == 1 and tree[nd][0] in visited:
                return 1 # count

            # take deepest two paths from the current node
            mx = [0, 0]          
            for ne in tree[nd]:
                if ne not in visited:
                    print(ne)
                    visited.add(ne)
                    k = dfs(ne)

                    if s[nd] != s[ne]:
                        heappush(mx, k)
                        heappop(mx)

            ans = max(ans, sum(mx) + 1)
            return max(mx) + 1
        
        dfs(0)
        return ans