class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, r, size = 0, len(s1) - 1, len(s2)
        cnt_1 = Counter(s1)
        cnt_2 = Counter(s2[l:r+1])

        while r < size:
            if cnt_1 == cnt_2: return True
            cnt_2[s2[l]] -= 1
            if r + 1 < size: cnt_2[s2[r + 1]] += 1

            l, r = l + 1, r + 1

        return False


