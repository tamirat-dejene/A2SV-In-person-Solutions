class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row_1 = set([c for c in "qwertyuiop"])
        row_2 = set([c for c in "asdfghjkl"])
        row_3 = set([c for c in "zxcvbnm"])
        ans = []
        for word in words:
            ws = set([w.lower() for w in word])
            if ws.issubset(row_1) or ws.issubset(row_2) or ws.issubset(row_3):
                ans.append(word)
        return ans

        