class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        # for all +ve integer if n % k == 0 and n <- the smallest possible: return len(str(x))

        seen_remainder, cnt = set(), 0
        start, rem = 1, 1 % k

        while True:
            rem = start % k
            if rem in seen_remainder: return -1
            start, cnt = rem * 10 + 1, cnt + 1
            
            if rem == 0: return cnt
            seen_remainder.add(rem)
        
        return cnt


        
