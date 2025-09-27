class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        wordSet = set(words)
        dp = [[False]*(len(words[i])) + [True] for i in range(len(words))]
        ans = []

        for i, word in enumerate(words):
            for j in range(len(word) - 1, -1, -1):
                for k in range(j, len(dp[i])):
                    if word[j:min(k, len(word))] in wordSet and dp[i][k] and word[j:k] != word:
                        dp[i][j] = True
                        break
            if dp[i][0]:
                ans.append(word)
        
        return ans