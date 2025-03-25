class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def valid(par):
            st = []
            for p in par:
                if p == '(':
                    st.append('(')
                else:
                    if st: st.pop()
                    else: return False
            
            return not st

        ans = []
        def dfs(store, o=0, c=0):
            if len(store) == 2 * n:
                par = ''.join(store)
                if valid(par): ans.append(par)
                return
            
            if o < n:
                store.append('(')
                dfs(store, o + 1, c)
                store.pop()

            if c < n:
                store.append(')')
                dfs(store, o, c + 1)
                store.pop()

        dfs([])

        return ans
        