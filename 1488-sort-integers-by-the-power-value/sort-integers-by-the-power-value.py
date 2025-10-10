class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        ans, store = [], {}
        
        for num in range(lo, hi + 1):
            if num not in store:
                stack = [num]

                while stack:
                    top = stack[-1]
                    top_log_2 = log2(top)

                    if top in store or top_log_2 == int(top_log_2):
                        top = stack.pop()
                        if top not in store:
                            store[top] = int(top_log_2)
            
                        while stack:
                            tmp = stack.pop()
                            store[tmp] = 1 + store[top]
                            top = tmp
                    else:
                        stack.append((3 * top + 1) if top % 2 == 1 else top // 2)
            
            heappush(ans, (store[num], num))
        
        while k > 1:
            heappop(ans)
            k -= 1
        
        return ans[0][1]