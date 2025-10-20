class Solution:
    def finalValueAfterOperations(self, ops: List[str], i=0) -> int:
        if i >= len(ops):
            return 0

        if ops[i] == 'X++' or ops[i] == '++X':
            return 1 + self.finalValueAfterOperations(ops, i + 1)
        else:
            return -1 + self.finalValueAfterOperations(ops, i + 1)
        
        
        