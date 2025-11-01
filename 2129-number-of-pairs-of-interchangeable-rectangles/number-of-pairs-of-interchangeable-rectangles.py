class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:

        ratios, ans = defaultdict(int), 0

        for w, h in rectangles:
            r = w / h
            ans += ratios[r]
            ratios[r] += 1
        
        return ans
        
        