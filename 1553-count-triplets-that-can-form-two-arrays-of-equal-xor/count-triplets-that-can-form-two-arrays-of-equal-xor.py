class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        ln = len(arr)
        cnt = 0

        a = 0 
        b = 0

        for i in range(ln - 1):
            a = 0

            for j in range(i + 1, ln):
                a ^= arr[j - 1]
                b = 0

                for k in range(j, ln):
                    b ^= arr[k]

                    if a == b:
                        cnt += 1
        
        return cnt
        