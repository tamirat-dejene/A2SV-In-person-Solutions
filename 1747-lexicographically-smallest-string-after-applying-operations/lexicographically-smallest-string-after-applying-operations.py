class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        ans, seen = s, set()

        def dfs(state):
            nonlocal ans
            string = ''.join(map(str, state))
            if string in seen:
                return

            ans = min(ans, string)            
            seen.add(string)
            
            # add
            add = state[:]
            for i in range(1, len(add), 2):
                add[i] = (add[i] + a) % 10
            dfs(add)
            
            # rotate
            rot = state[len(state) - b:] + state[:len(state) - b]
            dfs(rot)

            # add, rotate
            add_rot = add[len(add) - b:] + add[:len(add) - b]
            dfs(add_rot)

            # rotate, add
            rot_add = rot[:]
            for i in range(1, len(rot_add), 2):
                rot_add[i] = (rot_add[i] + a) % 10
            dfs(rot_add)
        
        dfs([int(si) for si in s])

        return ans