class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        N, vis = len(parents), set()
        tree = [[] for _ in range(N)]
        for nd in range(N):
            if parents[nd] != -1:
                tree[parents[nd]].append(nd)
        counter = Counter()
        def dfs(nd):
            cnt = 0
            for ne in tree[nd]:
                if ne not in vis:
                    vis.add(ne)
                    cnt += dfs(ne)
            counter[nd] = cnt + 1
            return 1 + cnt
        dfs(0)

        ans = [0] * N
        def dfs2(pr, ch):
            a = 1 if pr == -1 else counter[0] - counter[ch]
            for ne in tree[ch]:
                if ne != pr:
                    a *= counter[ne]

                    dfs2(ch, ne)
            ans[ch] = a
        dfs2(-1, 0)
        
        return ans.count(max(ans))
