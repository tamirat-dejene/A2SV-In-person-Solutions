class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ln = len(s)
        ans = []
        def dfs(p, store):
            if p == ln:
                if len(store) == 4:
                    ans.append('.'.join(store))
                return

            for i in range(p, ln):
                curr = s[p:i+1]
                
                if int(curr) > 255 or (curr != '0' and curr[0] == '0'): return
                store.append(curr)
                dfs(i + 1, store)
                store.pop()
        
        dfs(0, [])

        return ans
                
        