class Encrypter:

    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
        self.keyval = {c: values[i] for i, c in enumerate(keys)}
        self.valkey = defaultdict(list)
        for i, v in enumerate(values):
            self.valkey[v].append(keys[i])

        self.store = {}
        for word in dictionary:
            curr = self.store
            for c in word:
                if c not in curr:
                    curr[c] = {}
                curr = curr[c]
            curr['end'] = True

    def encrypt(self, word1: str) -> str:
        return ''.join(self.keyval[c] for c in word1)
    

    def decrypt(self, word2: str) -> int:

        def dfs(node, i):
            if i == len(word2):
                return 'end' in node
            
            cnt = 0
            ss = word2[i] + word2[i + 1]

            for k in self.valkey[ss]:
                if k in node:
                    cnt += dfs(node[k], i + 2)
            
            return cnt
        
        return dfs(self.store, 0)


# Your Encrypter object will be instantiated and called as such:
# obj = Encrypter(keys, values, dictionary)
# param_1 = obj.encrypt(word1)
# param_2 = obj.decrypt(word2)