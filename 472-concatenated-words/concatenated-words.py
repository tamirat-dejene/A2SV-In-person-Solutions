class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        # Bottom up solution
        
        # wordSet = set(words)
        # dp = [[False]*(len(words[i])) + [True] for i in range(len(words))]
        # ans = []
        # for i, word in enumerate(words):
        #     for j in range(len(word) - 1, -1, -1):
        #         for k in range(j, len(dp[i])):
        #             if word[j:min(k, len(word))] in wordSet and dp[i][k] and word[j:k] != word:
        #                 dp[i][j] = True
        #                 break
        #     if dp[i][0]:
        #         ans.append(word)
        # return ans


        # Top down, backtracking solution

        wordSet = set(words)

        def can_form_dfs(word, i=0, store=None):
            if i == len(word):
                return True
            
            if not store:
                store = [-1] * len(word)

            if store[i] == -1:
                for j in range(i, len(word)):
                    sub_word = word[i:j+1]

                    store[i] = can_form_dfs(word, j + 1, store) and word != sub_word and sub_word in wordSet
                    if store[i]:
                        break

                if store[i] == -1:
                    store[i] = False
            
            return store[i]
        
        return [word for word in words if can_form_dfs(word)]