class Solution:
    def getLucky(self, s: str, k: int) -> int:
        asciid = ''.join([str(ord(c) - 96) for c in s])
        for i in range(k):
            asciid = str(sum([int(n) for n in asciid]))
        return int(asciid)
        