class MapSum:

    def __init__(self):
        self.tree = {}

    def insert(self, key: str, val: int) -> None:
        curr = self.tree
        for c in key:
            if c not in curr:
                curr[c] = {}
            curr = curr[c]

        curr['val'] = val

    def search(self, prefix):
        curr = self.tree
        for c in prefix:
            if c not in curr:
                return -1
            curr = curr[c]
        return curr

    def sum(self, prefix: str) -> int:
        root = self.search(prefix)
        if root == -1:
            return 0
        # dfs
        tot, stack = 0, [root]

        while stack:
            curr = stack.pop()
            for c in curr:
                if c == 'val':
                    tot += curr[c]
                else:
                    stack.append(curr[c])
        print('--')
        return tot


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)