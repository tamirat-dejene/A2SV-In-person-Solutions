class Solution:
    def canCross(self, stones: List[int]) -> bool:
        positions = set(stones)
        store = {}
        def dfs(pos, last_jmp):
            if pos >= stones[-1]:
                return pos == stones[-1]

            
            if (pos, last_jmp) not in store:
                can_jmp = False

                if pos + last_jmp in positions:
                    can_jmp = dfs(pos + last_jmp, last_jmp)
                
                if not can_jmp and pos + last_jmp - 1 in positions and last_jmp >= 2:
                    can_jmp = dfs(pos + last_jmp - 1, last_jmp - 1)
                
                if not can_jmp and pos + last_jmp + 1 in positions:

                    can_jmp = dfs(pos + last_jmp + 1, last_jmp + 1)
                
                store[(pos, last_jmp)] = can_jmp
            
            return store[(pos, last_jmp)]

        return stones[1] == 1 and dfs(1, 1)        