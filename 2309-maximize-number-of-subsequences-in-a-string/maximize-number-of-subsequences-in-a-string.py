class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        p0 = list(accumulate([1 if c == pattern[0] else 0 for c in text]))
        p1 = list(accumulate([1 if c == pattern[1] else 0 for c in text[::-1]]))[::-1]

        # add pattern[0] to the beginning
        ans0 = p1[0] + sum(p1[i] - (1 if pattern[0] == pattern[1] else 0) for i in range(len(text)) if text[i] == pattern[0])
        # add pattern[1] to the end
        ans1 = p0[-1] + sum(p0[i] -  (1 if pattern[0] == pattern[1] else 0) for i in range(len(text)) if text[i] == pattern[1])

        return max(ans0, ans1)