class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack, cnt = [], Counter(s)
        taken = set()

        for c in s:
            
            while stack and c < stack[-1] and cnt[stack[-1]] > 0 and c not in taken:
                taken.remove(stack.pop())
            
            if c not in taken:
                stack.append(c)
            
            taken.add(c)
            cnt[c] -= 1

       

        return ''.join(stack)