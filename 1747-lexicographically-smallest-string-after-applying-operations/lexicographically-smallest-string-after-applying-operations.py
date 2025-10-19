class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        ans, seen = s, set()
        stack = [[int(si) for si in s]]


        while stack:
            state = stack.pop()
            string = ''.join(map(str, state))
            if string in seen:
                continue

            ans = min(ans, string)            
            seen.add(string)
            
            # add
            add = state[:]
            for i in range(1, len(add), 2):
                add[i] = (add[i] + a) % 10
            stack.append(add)
            
            # rotate
            rot = state[len(state) - b:] + state[:len(state) - b]
            stack.append(rot)

            # add, rotate
            add_rot = add[len(add) - b:] + add[:len(add) - b]
            stack.append(add_rot)

            # rotate, add
            rot_add = rot[:]
            for i in range(1, len(rot_add), 2):
                rot_add[i] = (rot_add[i] + a) % 10
            stack.append(rot_add)

        return ans