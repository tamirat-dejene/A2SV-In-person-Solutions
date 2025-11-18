class Solution:
    def grayCode(self, n: int) -> List[int]:
        ans = [0]
        taken = set([0])

        def dfs(curr, cnt):
            if cnt == 0:
                return bin(ans[0] ^ ans[-1]).count('1') == 1

            s = 1
            for i in range(n):
                tmp = curr ^ s
                if tmp not in taken:
                    ans.append(tmp)
                    taken.add(tmp)
                    if dfs(ans[-1], cnt - 1):
                        return True
                    ans.pop()
                    taken.remove(tmp)
                s <<= 1

            return False
    
        dfs(0, 2**n - 1)
        return ans
