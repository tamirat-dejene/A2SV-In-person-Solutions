class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        md = [a % k for a in arr]
        cnt = Counter(md)
        c = 0

        for m in md:
            if(m != k - m and cnt[m] > 0 and cnt[k - m] > 0) or (m == k - m and cnt[m] >= 2):
                c += 1
                cnt[m] -= 1
                cnt[k - m] -= 1

        return c + cnt[0] // 2 == len(arr) // 2