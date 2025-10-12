class TrieNode:
    def __init__(self, size):
        self.is_end_of_word = False
        self.alphabets = [False] * size

class Trie:
    def __init__(self, dictionary, alphabets):
        self.idx = dictionary
        self.size = len(dictionary)
        self.root = TrieNode(len(dictionary))
        self.alphabets = alphabets
    
    def insert(self, word):
        i, N = 0, len(word)
        root, substr = self.root, []

        while i < N:
            curr = ''.join(substr + [word[i]])
            if curr in self.idx:
                substr = [curr]
            else:
                # insert previous
                idx = self.idx[''.join(substr)]
                root.alphabets[idx] = root.alphabets[idx] or TrieNode(self.size)
                root = root.alphabets[idx]
                substr = [word[i]]
            
            if i == N - 1:
                # insert previous
                idx = self.idx[''.join(substr)]
                root.alphabets[idx] = root.alphabets[idx] or TrieNode(self.size)
                root = root.alphabets[idx]
                root.is_end_of_word = True
            
            i += 1
        
    def inorder(self, curr):
        alphabets = self.alphabets

        res = []
        for i in range(self.size):
            if curr.alphabets[i]:
                suffixes = self.inorder(curr.alphabets[i])

                # if the non leaf is end of word
                if curr.alphabets[i].is_end_of_word and sum(1 for i in curr.alphabets[i].alphabets if i):
                    res.append([alphabets[i]])

                for suff in suffixes:
                    res.append([alphabets[i]] + suff)
    
        return [[]] if not res else res

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dictionary = {word: i for i, word in enumerate(order)}
        cnt = Counter(words)

        trie = Trie(dictionary, order)
        for word in words:
            trie.insert(word)
        
        io = trie.inorder(trie.root)
        srted = []

        for wo in io:
            wo = ''.join(wo)
            srted.extend([wo] * cnt[wo])

        return words == srted
