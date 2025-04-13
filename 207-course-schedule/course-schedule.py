class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # circular dependecncy
        graph = defaultdict(list)
        for c, p in prerequisites:
            graph[c].append(p)

        gvis, lvis = set(), set()

        def cycle(node):
            gvis.add(node)
            lvis.add(node)

            for p in graph[node]:
                if (p not in gvis and cycle(p)) or p in lvis:
                    return True
            
            lvis.remove(node)
            return False

        for c in range(numCourses):
            if c not in gvis and cycle(c):
                return False
        
        return True


        

        