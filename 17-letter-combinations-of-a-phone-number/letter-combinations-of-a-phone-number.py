class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hmap = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }

        if not digits: return []

        ans = []
        ln = len(digits)

        def dfs(p, store):
            if p == ln:
                ans.append(''.join(store))
                return
            curr = digits[p]

            for ch in hmap[curr]:
                store.append(ch)
                dfs(p + 1, store)
                store.pop()
        
        dfs(0, [])

        return ans
            


        
        