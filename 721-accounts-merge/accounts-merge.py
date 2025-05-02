class UnionFind:
    def __init__(self, accounts):
        self.size = [len(account) for account in accounts]
        self.root = [n for n in range(len(accounts))]
    
    def find(self, nd):
        while nd != self.root[nd]:
            self.root[nd] = self.root[self.root[nd]]
            nd = self.root[nd]  
        
        return nd

    def union(self, nd1, nd2):
        rt1 = self.find(nd1)
        rt2 = self.find(nd2)

        if rt1 == rt2: return False

        if self.size[rt1] >= self.size[rt2]:
            self.root[rt2] = rt1
            self.size[rt1] += self.size[rt2]
        else:
            self.root[rt1] = rt2
            self.size[rt2] += self.size[rt1]

        return True

    def connected(self, nd1, nd2):
        return self.find(nd1) == self.find(nd2)

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(accounts)
        emails = defaultdict(list)

        for i, account in enumerate(accounts):
            for j in range(1, len(account)):
                emails[account[j]].append(i)

        for e in emails:
            for i in range(1, len(emails[e])):
                ow1, ow2 = emails[e][i - 1], emails[e][i]
                uf.union(ow1, ow2)
        
        owners = defaultdict(set)

        for i, account in enumerate(accounts):
            ow = uf.find(i)
            for j in range(1, len(account)):
                owners[ow].add(account[j])
        
        res = []

        for ow in owners:
            acc = [accounts[ow][0]]
            acc.extend(sorted(owners[ow]))
            res.append(acc)

        return res

