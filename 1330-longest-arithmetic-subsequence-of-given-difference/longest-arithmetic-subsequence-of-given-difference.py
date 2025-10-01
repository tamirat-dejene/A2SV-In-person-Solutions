class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        N = len(arr)
        dp = [1] * N
        idx= dict()
        for l in range(N - 1, -1, -1):
            if difference + arr[l] in idx:
                r = idx[difference + arr[l]]
                dp[l] = max(1 + dp[r], dp[l])
            
            idx[arr[l]] = l
        
        return max(dp)

        store = [-1] * len(arr)

        def dfs(i):
            if i >= len(arr):
                return 0
            
            if store[i] == -1:

                store[i] = 1
                for j in range(i + 1, len(arr)):
                    if difference == arr[j] - arr[i]:
                        store[i] += dfs(j)    
                
                store[i] = max(store[i], dfs(i + 1))

            return store[i]
        
        return dfs(0)

            


        