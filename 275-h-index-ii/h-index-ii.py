class Solution:
    def hIndex(self, citations: List[int]) -> int:
        N = len(citations)
        l, r = -1, N

        while l + 1 < r:
            m = (l + r) // 2

            if citations[m] >= N - m:
                r = m
            else:
                l = m
        
        return N - r
        