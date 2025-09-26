class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        longest_word = max(len(word) for word in wordDict)
        dictionary = set(wordDict)
        store = defaultdict(bool)

        def dfs(i):
            if i == len(s):
                return True
            
            if i not in store:
            
                for j in range(i, min(i + longest_word, len(s))):
                    if s[i:j+1] in dictionary and dfs(j + 1):
                        store[i] = True
                
                if i not in store:
                    store[i] = False

            return store[i]

        return dfs(0)        