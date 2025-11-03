class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        ans = 0
        l, r = 0, 0
        N = len(colors)
        
        while r < N:
            sm = 0
            mx = 0

            while r < N and colors[r] == colors[l]:
                sm += neededTime[r]
                mx = max(neededTime[r], mx)
                r += 1
            
            if r - l > 1:
                ans += (sm - mx)
            l = r
        
        return ans