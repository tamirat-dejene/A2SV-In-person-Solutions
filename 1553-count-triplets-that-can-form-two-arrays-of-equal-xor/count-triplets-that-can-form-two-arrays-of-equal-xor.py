class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        ln = len(arr)
        cnt = 0

        a = 0 
        b = 0

        for i in range(ln - 1):
            a = arr[i]

            for j in range(i + 1, ln):
                a ^= arr[j]
                b = arr[j]

                for k in range(j, ln):
                    b ^= arr[k]

                    if a == b:
                        cnt += 1
        
        return cnt
        