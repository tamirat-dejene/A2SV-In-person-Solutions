class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []

        for b in s:
            if b == '(':
                stack.append(b)
            else:
                sm = 0
                while stack and stack[-1] != '(':
                    sm += stack.pop()
                
                sm = (sm * 2) if sm != 0 else 1
                stack.pop()
                stack.append(sm)
        
        return sum(stack)

        