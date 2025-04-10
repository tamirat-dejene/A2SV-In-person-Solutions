class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        distance = lambda x1, y1, x2, y2: ((x2 - x1)**2 + (y2 - y1)**2)**0.5
        graph = defaultdict(list)

        for i in range(n):
            for j in range(i + 1, n):
                x1, y1, r1 = bombs[i]
                x2, y2, r2 = bombs[j]
                dis = distance(x1, y1, x2, y2)
                if dis <= r1:
                    graph[i].append(j)
                if dis <= r2:
                    graph[j].append(i)
                    
        def dfs(curr, visited):
            cnt = 1
            for b in graph[curr]:
                if b not in visited:
                    visited.add(b)
                    cnt += dfs(b, visited)

            return cnt
        
        ans = 1
        for b in range(n):
            ans = max(ans, dfs(b, set([b])))
            if ans == n: return n
        
        return ans
