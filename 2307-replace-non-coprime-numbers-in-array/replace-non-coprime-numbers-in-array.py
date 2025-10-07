class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = []

        for num in nums:
            stack.append(num)

            while len(stack) >= 2:
                a, b = stack.pop(), stack.pop()
                g_d = gcd(a, b) 
                if g_d != 1:
                    stack.append(a * b // g_d)
                else:
                    stack.append(b)
                    stack.append(a)
                    break

        
        return stack

        