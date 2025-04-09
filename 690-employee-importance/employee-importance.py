"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        graph = defaultdict(list)
        emps = defaultdict(int)

        for emp in employees:
            emps[emp.id] = emp.importance
            for semp in emp.subordinates:
                graph[emp.id].append(semp)

        visited = set()

        def dfs(curr):
            tot = emps[curr]


            for sub in graph[curr]:
                if sub not in visited:

                    visited.add(sub)
                    tot += dfs(sub)

            return tot            
        
        return dfs(id)