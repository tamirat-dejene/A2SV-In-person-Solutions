class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        MD = 1_000_000_007
        count = []
        cy = Counter()

        for x, y in points:
            cy[y] += 1
        for y in cy:
            count.append(cy[y] * (cy[y] - 1) // 2)

        psum = list(accumulate(count))
        ans = 0

        for i in range(len(count) - 1, 0, -1):
            ans += count[i] * psum[i - 1]
            ans %= MD
        
        return ans


            