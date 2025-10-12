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
    # Solution 1
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dictionary = {word: i for i, word in enumerate(order)}

        def compare(word1, word2, l1=0, l2=0):
            M, N = len(word1), len(word2)
            
            if l1 == M: return -1 # word1 end
            if l2 == N: return 1 # word2 end

            r1, r2 = l1, l2
            for r in range(M, l1, -1):
                if word1[l1:r] in dictionary:
                    r1 = r
                    break
                    
            for r in range(N, l2, -1):
                if word2[l2:r] in dictionary:
                    r2 = r
                    break

            a = dictionary[word1[l1:r1]]
            b = dictionary[word2[l2:r2]]

            return -1 if a < b else 1 if a > b else compare(word1, word2, r1, r2)

        srted = sorted(words, key=cmp_to_key(compare))

        return srted == words

    # def isAlienSorted(self, words: List[str], order: str) -> bool:
    #     cnt = Counter(words)

    #     trie = Trie(order)
    #     for word in words:
    #         trie.insert(word)
        
    #     io, srted = trie.inorder(trie.root), []

    #     for wo in io:
    #         wo = ''.join(wo)
    #         srted.extend([wo] * cnt[wo])
        
    #     return words == srted
