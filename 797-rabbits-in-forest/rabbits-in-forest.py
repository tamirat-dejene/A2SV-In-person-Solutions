class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)

        res = 0
        def ceil_div(x, y): return (x + y - 1) // y

        for ans, cnt in count.items():
            res += (ans + 1) * ceil_div(cnt, ans + 1)
        
        return res


        

