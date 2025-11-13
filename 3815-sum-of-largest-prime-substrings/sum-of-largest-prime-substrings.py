class Solution:
    def sumOfLargestPrimes(self, s: str) -> int:
        N = len(s)
        ss = set()

        def isprime(num):
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    return False 
            return num > 1


        for i in range(N):
            for j in range(i, N):
                if isprime(int(s[i:j+1])):
                    ss.add(int(s[i:j+1]))

        ls = sorted(ss)  
        if len(ls) <= 3:
            return sum(ls)
        return ls[-1] + ls[-2] + ls[-3]
