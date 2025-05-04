"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        
        def build(tlr, tlc, brr, brc):
            if tlc == brc and tlr == brr: 
                return Node(grid[tlr][tlc], True, None, None, None, None)

            val = grid[tlr][tlc]
            all_same = True

            for r in range(tlr, brr + 1):
                for c in range(tlc, brc + 1):
                    if grid[r][c] != val:
                        all_same = False
                        break

                if not all_same: break
            
            if all_same: 
                return Node(val, True, None, None, None, None)

            mid_r = (tlr + brr) // 2
            mid_c = (tlc + brc) // 2

            tl = build(tlr, tlc, mid_r, mid_c)
            tr = build(tlr, mid_c + 1, mid_r, brc)
            bl = build(mid_r + 1, tlc, brr, mid_c)
            br = build(mid_r + 1, mid_c + 1, brr, brc)

            return Node(val, False, tl, tr, bl, br)

        return build(0, 0, len(grid) - 1, len(grid) - 1)




                    

        