class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        N, ans = len(s), [""]
        close = list(accumulate([1 if s[i] == ')' else 0 for i in range(N)][::-1]))[::-1]

        def dfs(l, stack, store):
            nonlocal ans

            if l == N or stack > close[l]:
                if stack == 0:
                    curr = ''.join(store)
                    if len(curr) > len(ans[0]):
                        ans = [curr]
                    elif len(curr) == len(ans[0]):
                        ans.append(curr)
                return
            
            if s[l] != ')' and s[l] != '(':
                store.append(s[l])
                dfs(l + 1, stack, store)
                return store.pop()
            
            # take
            if not (s[l] == ')' and stack == 0):
                stack += (1 if s[l] == '(' else -1)
                store.append(s[l])

                dfs(l + 1, stack, store)

                stack += (-1 if s[l] == '(' else 1)
                store.pop()

            # leave
            dfs(l + 1, stack, store)

        dfs(0, 0, [])
        return list(set(ans))