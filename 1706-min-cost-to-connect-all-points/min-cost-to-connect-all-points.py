class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        root = [i for i in range(len(points))]
        size = [1] * len(points)

        hp = []
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                heappush(hp, (abs(x1 - x2) + abs(y1 - y2), i, j))


        def find(nd):
            while nd != root[nd]:
                root[nd] = root[root[nd]]
                nd = root[nd]  
            
            return nd
        
        def union(a, b):
            p1 = find(a)
            p2 = find(b)

            if p1 == p2: return False

            if size[p1] >= size[p2]:
                size[p1] += size[p2]
                root[p2] = p1
            else:
                size[p2] += size[p1]
                root[p1] = p2
            
            return True

        wdgt = 0 
        e = 0

        while hp:
            if e == len(points) - 1:
                break
            w, i, j = heappop(hp)  
        

            if union(i, j):
                wdgt += w
                e += 1
        
        return wdgt

