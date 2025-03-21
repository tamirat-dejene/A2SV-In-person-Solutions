class Solution:
    def validStrings(self, n: int) -> List[str]:
        ans = []

        def dfs(string=[]):
            nonlocal n

            if len(string) == n:
                ans.append("".join(string))
                return

            if not string or string[-1] == "1":
                string.append("0")
                dfs(string)
                string.pop()
            
            string.append("1")
            dfs(string)
            string.pop()
        
        dfs()

        return ans