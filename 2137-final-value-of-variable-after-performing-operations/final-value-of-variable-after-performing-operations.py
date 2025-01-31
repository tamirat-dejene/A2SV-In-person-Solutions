class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        start=0
        for op in operations:
            if op == '--X' or op == 'X--': start -= 1
            elif op == '++X' or op == 'X++': start += 1
        return start
        