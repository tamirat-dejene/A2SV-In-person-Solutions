class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        # store = [[0]*N for _ in range(N)]

        # def dfs(p, c):
        #     if c >= N:
        #         return 0

        #     if not store[p][c]:
        #         store[p][c] = 1

        #         if p == -1 or nums[c] > nums[p]:
        #             # leave or take
        #             store[p][c] = max(dfs(p, c + 1), 1 + dfs(c, c + 1))
        #         else:
        #             # leave
        #             store[p][c] = dfs(p, c + 1)

        #     return store[p][c]

        # return dfs(-1, 0)
        res = []

        for num in nums:
            pos = bisect_left(res, num)
            if pos == len(res):
                res.append(num)
            else:
                res[pos] = num

        return len(res)

        store = [1] * N
        for l in range(N - 1, -1, -1):
            for r in range(l + 1, N):
                if nums[l] < nums[r]:
                    store[l] = max(store[l], 1 + store[r])

        return max(store)