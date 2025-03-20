class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        
        cookies.sort(reverse=True)
        ans = float('inf')
        
        def dfs(ck, children):
            nonlocal ans
            # base, all the cookies distributed
            if ck == len(cookies):
                ans = min(ans, max(children))
                return

            for c in range(k):
                if children[c] + cookies[ck] >= ans: continue

                children[c] += cookies[ck]
                dfs(ck + 1, children)
                children[c] -= cookies[ck]

                if children[c] == 0: break
        
        dfs(0, [0]*k)

        return ans