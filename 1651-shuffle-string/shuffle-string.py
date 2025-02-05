class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans = ['']*len(s)
        for i, j in enumerate(indices):
            ans[j] = s[i]
        return ''.join(ans)