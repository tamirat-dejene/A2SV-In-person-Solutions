class Solution:
    def smallestNumber(self, pattern: str) -> str:
        stack = []
        ans = []
        for i, p in enumerate(pattern):

            if p == 'D':
                stack.append(i + 1)
            else:
                ans.append(i + 1)

            while stack and p == 'I':
                ans.append(stack.pop())

            
        ans.append(len(pattern) + 1)
        while stack: ans.append(stack.pop())

        return ''.join(str(n) for n in ans)


        