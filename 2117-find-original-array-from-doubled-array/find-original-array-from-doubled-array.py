class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        i, j, size = 0, 1, len(changed)
        if size % 2 == 1: return []
        changed.sort()
        
        while i < size:
            if changed[i] == None: 
                i += 1
                if j <= i: j = i + 1
            else:
                found = False
                while j < size:
                    if changed[j] == 2 * changed[i]:
                        found = True
                        changed[j] = None
                        break
                    j += 1
                if not found: changed[i] = None
                i += 1

        filtered = [o for o in changed if o is not None]
        return [] if len(filtered) != size // 2 else filtered
        