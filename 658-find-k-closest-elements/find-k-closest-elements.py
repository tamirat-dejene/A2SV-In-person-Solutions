class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        hp = [(abs(x - a), a) for a in arr]
        heapify(hp)

        res = []

        while True:
            if len(res) == k: 
                return sorted(res)

            _, v = heappop(hp)
            res.append(v)
        


        