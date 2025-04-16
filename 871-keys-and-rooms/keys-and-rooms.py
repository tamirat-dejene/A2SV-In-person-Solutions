class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        queue = deque([0])
        visited = set([0])

        while queue:
            r = queue.popleft()
            for k in rooms[r]:
                if k not in visited:
                    visited.add(k)
                    queue.append(k)
        
        return set(range(len(rooms))) == visited