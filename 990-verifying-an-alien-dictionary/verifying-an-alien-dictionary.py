class TrieNode:
    def __init__(self):
        self.is_end_of_word = False
        self.alphabets = [False] * 26

class Trie:
    def __init__(self, alphabets):
        self.idx = {alph: i for i, alph in enumerate(alphabets)}
        self.root = TrieNode()
        self.alphabets = alphabets
    
    def insert(self, word):
        i, N, root = 0, len(word), self.root

        for c in word:
            idx = self.idx[c]
            root.alphabets[idx] = root.alphabets[idx] or TrieNode()
            root = root.alphabets[idx]
        root.is_end_of_word = True

    def inorder(self, curr):
        res = []
        
        for i in range(26):
            if curr.alphabets[i]:
                suffixes = self.inorder(curr.alphabets[i])

                # if the non leaf is end of word
                if curr.alphabets[i].is_end_of_word and sum(1 for i in curr.alphabets[i].alphabets if i):

                    res.append([self.alphabets[i]])

                for suff in suffixes:
                    res.append([self.alphabets[i]] + suff)
    
        return [[]] if not res else res

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        cnt = Counter(words)

        trie = Trie(order)
        for word in words:
            trie.insert(word)
        
        io, srted = trie.inorder(trie.root), []

        for wo in io:
            wo = ''.join(wo)
            srted.extend([wo] * cnt[wo])
        
        return words == srted
