class Solution:
    def countGoodNodes(self, edges: List[List[int]]) -> int:
        tree = [[] for _ in range(len(edges) + 1)]

        for a, b in edges:
            tree[a].append(b)
            tree[b].append(a)

        vis = set([0])

        def dfs(nd):
            # leaf node
            if len(tree[nd]) == 1 and tree[nd][0] in vis:
                return 1, 1 # total nodes in the subtree, total good nodes in the subtree

            goods = 0 # count of good subtrees
            nodes = 1 # total nodes for the subtree
            cnodes = -1 # count of nodes for each child
            good_st = 1

            for ch in tree[nd]:
                if ch not in vis:
                    vis.add(ch)

                    cnt, gods = dfs(ch)

                    if cnodes != -1 and cnodes != cnt:
                        good_st = 0
                    
                    goods += gods
                    cnodes = cnt
                    nodes += cnodes

            return nodes, goods + good_st

        return dfs(0)[1]