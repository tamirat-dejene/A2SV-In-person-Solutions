class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []

        def dfs(store=[], sm=0):
            nonlocal target

            if sm >= target:
                if sm == target: ans.append(sorted(store))
                return

            for cd in candidates:
                store.append(cd)
                dfs(store, sm + cd)
                store.pop()

        dfs()

        return list(set(map(tuple, ans)))
        