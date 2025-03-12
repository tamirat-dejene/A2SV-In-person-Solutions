class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def get_binary(n, k, f=0):            
            if n == 1: return 0 if f % 2 == 0 else 1
            return get_binary(n - 1, k if k <= 2**(n - 2) else 2**(n - 2) - 2**(n - 1) + k, f + 1 if k > 2**(n - 2) else f)
            
        return get_binary(n, k)
            

        