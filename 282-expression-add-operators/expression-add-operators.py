class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        N = len(num)

        def evaluate(exp, i, fullexp):
            if i == len(exp):
                e = ''.join(fullexp)
                return [e] if target == eval(e) else []

            res = []   
            if not fullexp:
                fullexp.append(exp[i])
                res.extend(evaluate(exp, i + 1, fullexp))
                return res

            for op in '+-*':
                fullexp.extend([op, exp[i]])
                res.extend(evaluate(exp, i + 1, fullexp))
                fullexp.pop()
                fullexp.pop()
            return res

        def dfs(i, exp):
            if i == N:
                return evaluate(exp, 0, [])
            
            ans = []
            if num[i] == '0':
                ans.extend(dfs(i + 1, exp + ['0']))
            else:
                for j in range(i, N):
                    exp.append(num[i:j+1])
                    ans.extend(dfs(j + 1, exp))
                    exp.pop()
        
            return ans
        
        return dfs(0, [])

            
        