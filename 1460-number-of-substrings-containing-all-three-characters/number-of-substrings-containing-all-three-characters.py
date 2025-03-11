class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        hmap = defaultdict(int)
        cnt = 0

        for i, c in enumerate(s):
            hmap[c] = i

            if len(hmap) == 3:
                cnt += min(hmap.get('a'), hmap.get('b'), hmap.get('c')) + 1
        
        return cnt

        