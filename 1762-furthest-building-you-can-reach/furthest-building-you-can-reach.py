class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        hp = []
        tot_brick = 0
        lad_brick = 0

        for i in range(1, len(heights)):
            jmp = heights[i] - heights[i - 1]
            if jmp <= 0: continue
            
            tot_brick += jmp
            if ladders > 0:
                heappush(hp, jmp)
                lad_brick += jmp
                ladders -= 1
            elif hp and jmp > hp[0]:
                lad_brick -= hp[0]
                lad_brick += jmp
                heapreplace(hp, jmp)
            
            if bricks < tot_brick - lad_brick: return i - 1
        
        return len(heights) - 1


        