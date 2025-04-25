class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        sz = len(quiet)
        graph = defaultdict(list)
        indegree = defaultdict(int)

        for pa, pb in richer:
            graph[pa].append(pb)
            indegree[pb] += 1
        
        queue = deque([n for n in range(sz) if n not in indegree])
        ans = [i for i in range(sz)]

        while queue:
            richer = queue.popleft()

            for rich in graph[richer]:
                if quiet[ans[richer]] < quiet[ans[rich]]:
                    ans[rich] = ans[richer]
                
                indegree[rich] -= 1
                if indegree[rich] == 0:
                    queue.append(rich)
            
        print(ans)
        return ans