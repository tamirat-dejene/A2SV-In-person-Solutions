class Solution:
    def minimumPushes(self, word: str) -> int:
        if len(word) <= 8:
            return len(word)
        
        ans = {
             9: 10,
            10: 12,
            11: 14,
            12: 16,
            13: 18,
            14: 20,
            15: 22,
            16: 24,
            17: 27,
            18: 30,
            19: 33,
            20: 36,
            21: 39,
            22: 42,
            23: 45,
            24: 48,
            25: 52,
            26: 56
        }

        return ans[len(word)]


        