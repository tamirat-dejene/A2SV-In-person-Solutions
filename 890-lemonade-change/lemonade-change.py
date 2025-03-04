class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        changes = defaultdict(int)

        for bill in bills:
            if changes[5] == 0: changes.pop(5)
            if changes[10] == 0: changes.pop(10)

            if bill == 5:
                changes[5] += 1
            elif bill == 10:
                if 5 not in changes: return False
                changes[5] -= 1
                changes[10] += 1
            else:
                if 5 not in changes or (10 not in changes and changes[5] < 3): return False
                if 10 in changes: 
                    changes[10] -= 1
                else:
                    changes[5] -= 2
                
                changes[5] -= 1
            
        return True