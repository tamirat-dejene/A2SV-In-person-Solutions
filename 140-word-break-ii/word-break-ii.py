class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        longest_word = max(len(word) for word in wordDict)
        dictionary = set(wordDict)
        store = defaultdict(list)
        ans = []
        def dfs(i, lst):
            if i == len(s):
                ans.append(lst[:])
                return lst
            
            for j in range(i, min(i + longest_word, len(s))):
                if s[i:j+1] in dictionary:
                    lst.append(s[i:j+1])
                    dfs(j + 1, lst)
                    lst.pop()

        dfs(0, [])
        return [' '.join(a) for a in ans]
        