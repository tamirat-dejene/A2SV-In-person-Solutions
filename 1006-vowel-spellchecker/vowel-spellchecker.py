class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        store = {}
        lowered = {}
        vow_rem = {}
        for i, word in enumerate(wordlist):
            if word not in store:
                store[word] = i
            if word.lower() not in lowered:
                lowered[word.lower()] = i

            vrm = ''.join([('_' if c.lower() in 'aeiou' else c.lower()) for c in word])

            if vrm not in vow_rem:
                vow_rem[vrm] = i
        

        ans = []
        for query in queries:
            if query in store:
                ans.append(wordlist[store[query]])
            elif query.lower() in lowered:
                ans.append(wordlist[lowered[query.lower()]])
            else:
                vrm = ''.join([('_' if c.lower() in 'aeiou' else c.lower()) for c in query])
                if vrm in vow_rem:
                    ans.append(wordlist[vow_rem[vrm]])
                else:
                    ans.append("")

        return ans