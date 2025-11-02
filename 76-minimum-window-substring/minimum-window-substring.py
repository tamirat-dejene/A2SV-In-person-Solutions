class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s_freq = Counter()
        t_freq = Counter(t)

        ans = (inf, inf, inf)
        N, l = len(s), 0
        M = len(t)

        for r in range(N):
            s_freq[s[r]] += 1
            
            while l <= r and (t_freq[s[l]] == 0 or s_freq[s[l]] > t_freq[s[l]]):
                s_freq[s[l]] -= 1
                l += 1

            if not any(s_freq[c] < t_freq[c] for c in t_freq):
                ans = min(ans, (r - l + 1, l, r))

        if ans[0] != inf:
            l, r = ans[1], ans[2]
            return s[l:r + 1]

        return ""
        