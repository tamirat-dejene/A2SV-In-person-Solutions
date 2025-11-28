class Solution:
    def componentValue(self, nums: List[int], edges: List[List[int]]) -> int:
        N, tot = len(nums), sum(nums)
        tree = [[] for _ in range(N)]
        mn = min(nums)
        
        for a, b in edges:
            tree[a].append(b)
            tree[b].append(a)
        
        def dfs(p, c, sm):
            cs = nums[c]

            for gc in tree[c]:
                if gc == p: continue

                val = dfs(c, gc, sm)
                if val == -1:
                    return -1
                cs += val
            
            return 0 if cs == sm else (-1 if cs > sm else cs)

        for ans in range(N, 0, -1):
            if tot % ans == 0 and tot // ans >= mn and dfs(-1, 0, tot // ans) == 0:
                return ans - 1

        return 0


