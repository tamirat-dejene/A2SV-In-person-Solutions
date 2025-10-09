class Node:
    def __init__(self):
        self.end_of_word = False
        self.nodes = [False] * 26

class Trie:
    def __init__(self):
        self.root = Node()
        

    def insert(self, word: str) -> None:
        curr = self.root

        for c in word:
            idx = ord(c) - ord('a')

            if not curr.nodes[idx]:
                curr.nodes[idx] = Node()

            curr = curr.nodes[idx]
        curr.end_of_word = True
        

    def search(self, word: str) -> bool:
        return self.srch(word)

    def startsWith(self, prefix: str) -> bool:
        return self.srch(prefix, True)

    def srch(self, word, prefix=False):
        temp = self.root

        for c in word:
            idx = ord(c) - ord('a')

            if not temp.nodes[idx]:
                return False
            temp = temp.nodes[idx]
        
        return prefix or temp.end_of_word
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)