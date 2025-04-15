class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        graph = defaultdict(set)
        for a, b in trust: graph[a].add(b)

        j = -1
        for i in range(1, n + 1):
            if i not in graph:
                if j != -1: return -1
                j = i
        
        if j == -1: return j

        for i in range(1, n + 1):
            if i != j:
                if j not in graph[i]: return -1
        
        return j
