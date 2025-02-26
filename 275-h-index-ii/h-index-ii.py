class Solution:
    def hIndex(self, citations: List[int]) -> int:
        s = len(citations)
        for i, citation in enumerate(citations):
            if citation >= s - i: return s - i
        
        return 0

        