class WordFilter:

    def __init__(self, words: List[str]):
        self.top_d = {} # top down tree
        self.btm_u = {} # bottom up tree

        words = {word: i for i, word in enumerate(words)} # unique

        for word in words:
            self.insert(words[word], word)
            self.insert(words[word], word[::-1], False)

    def insert(self, i, word, top_d=True):
        curr = self.top_d if top_d else self.btm_u

        for c in word:
            if c not in curr:
                curr[c] = {}
            curr = curr[c]
            
            if 'idx' not in curr:
                curr['idx'] = set()
            curr['idx'].add(i)

    def search(self, sub, pref=True):
        curr = self.top_d if pref else self.btm_u
        for c in sub:
            if c not in curr:
                return set() # indices
            curr = curr[c]
        
        return curr['idx']
            
    def f(self, pref: str, suff: str) -> int:
        p = self.search(pref)
        s = self.search(suff[::-1], pref=False)

        common = p.intersection(s)
        if not common:
            return -1
        else:
            return max(common)

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)