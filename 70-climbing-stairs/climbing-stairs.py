class Solution:
    def climbStairs(self, n: int) -> int:
        '''
                5
               / \
              4   3
             / \  / \
            2   3 2  1
           /   / \ \ 
          1   2   1 1
             /
            1
        '''
        store = {
            1: 1,
            2: 2
        }

        def f(k):
            if k not in store:
                store[k] = f(k - 1) + f(k - 2)
                
            return store[k]

        return f(n)
        