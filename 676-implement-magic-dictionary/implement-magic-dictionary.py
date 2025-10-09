class Node:
    def __init__(self):
        self.nodes = [False] * 26
        self.is_end_of_word = False

class MagicDictionary:
    def __init__(self):
        self.dictionary = Node()

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.insert(word)

    def search(self, searchWord: str) -> bool:
        curr, found = self.dictionary, True

        for i in range(len(searchWord)):
            idx = ord(searchWord[i]) - ord('a')
            if not curr.nodes[idx]:
                found = False
            
            for j in range(26):
                if j != idx and curr.nodes[j] and self.helper_search(curr.nodes[j], i + 1, searchWord):
                    return True
            
            if not found:
                return False
            curr = curr.nodes[idx]
            
        return False

    def helper_search(self, root, i, word):
        for j in range(i, len(word)):
            idx = ord(word[j]) - ord('a')
            if not root.nodes[idx]:
                return False
            root = root.nodes[idx]

        return root.is_end_of_word

    def insert(self, word):
        curr = self.dictionary

        for c in word:
            idx = ord(c) - ord('a')
            
            if not curr.nodes[idx]:
                curr.nodes[idx] = Node()
            
            curr = curr.nodes[idx]

        curr.is_end_of_word = True
        


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)