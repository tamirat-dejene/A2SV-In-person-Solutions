class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        par = defaultdict(chr)
        cnt = defaultdict(int)

        def find(node):
            if node == par[node]:
                return node
            par[node] = find(par[node])
            return par[node]
        
        def union(node1, node2):
            p1, p2 = find(node1), find(node2)
            if p1 == p2: return False

            if cnt[p1] >= cnt[p2]:
                cnt[p1] += cnt[p2]
                par[p2] = p1
            else:
                cnt[p2] += cnt[p1]
                par[p1] = p2
            
            return True
        
        store = []
        
        for eqn in equations:
            opd1, opd2, comp = eqn[0], eqn[-1], eqn[1:3]
            store.append((opd1, opd2, comp))

            if opd1 not in par:
                par[opd1] = opd1
                cnt[opd1] = 1
            if opd2 not in par:
                par[opd2] = opd2
                cnt[opd2] = 1

            if comp == '==':
                union(opd1, opd2)
        
        for opd1, opd2, comp in store:
            p1, p2 = find(opd1), find(opd2)

            if (p1 == p2 and comp == '!=') or (p1 != p2 and comp == '=='):
                return False

        return True        

            
                



        