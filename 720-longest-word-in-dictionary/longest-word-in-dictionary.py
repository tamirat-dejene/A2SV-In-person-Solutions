class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = {}

        for word in words:
            curr = trie
            for c in word:
                if c not in curr:
                    curr[c] = {}
                curr = curr[c]
            curr['end'] = True
        
        ans = ''

        for c in sorted(trie.keys()):
            stack = [(trie[c], [c])]

            while stack:
                curr, store = stack.pop()

                if 'end' not in curr:
                    if len(store) > len(ans):
                        if store:
                            store.pop()
                        tmp = ''.join(store)

                        ans = min(ans, tmp) if len(ans) == len(tmp) else tmp
                    continue
                
                if len(store) > 1 and len(store) > len(ans):
                    tmp = ''.join(store)
                    ans = min(ans, tmp) if len(ans) == len(tmp) else tmp

                for cc in sorted(curr.keys(), reverse=True):
                    if cc != 'end':
                        stack.append((curr[cc], store + [cc]))
        return ans