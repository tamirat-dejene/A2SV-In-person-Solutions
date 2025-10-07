class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        cnt = 0

        for c in s:
            if not stack or stack[-1][0] == c:
                cnt += 1
                stack.append((c, cnt))
            else:
                stack.append((c, 1))
                cnt = 1
            
            if cnt == k:
                while cnt > 0:
                    stack.pop()
                    cnt -= 1
                if stack:
                    cnt = stack[-1][1]
        
        return ''.join(st[0] for st in stack)