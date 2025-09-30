class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # BU DP
        N = len(s)
        longest_word = max(len(word) for word in wordDict)
        dictionary = set(wordDict)

        dp = [False] * (N + 1)
        dp[N] = True

        for i in range(N - 1, -1, -1):
            for j in range(i, min(i + longest_word, N)):
                if s[i:j+1] in dictionary and dp[j + 1]:
                    dp[i] = True
        
        return dp[0]



        # TD DP

        store = defaultdict(bool)
        def dfs(i):
            if i == N:
                return True
            
            if i not in store:
                for j in range(i, min(i + longest_word, N)):
                    if s[i:j+1] in dictionary and dfs(j + 1):
                        store[i] = True
                
                if i not in store:
                    store[i] = False

            return store[i]

        return dfs(0)        