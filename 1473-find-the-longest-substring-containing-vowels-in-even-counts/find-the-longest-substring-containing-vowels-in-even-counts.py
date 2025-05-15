class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        store = defaultdict(int)
        store[0] = -1

        vowels = {
            'a': 1,
            'e': 2,
            'i': 4,
            'o': 8,
            'u': 16
        }

        pref = 0
        ans = 0

        for i in range(len(s)):
            if s[i] in vowels:
                pref ^= vowels[s[i]]

            if pref in store:
                ans = max(ans, i - store[pref])
            else:
                store[pref] = i

        return ans                