class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        lft, rgt = min(nums), max(nums)

        line = [0] * (len(nums) + 1)
        
        for l, r in requests:
            line[l] += 1
            line[r + 1] -= 1

        for i in range(1, len(line)):
            line[i] += line[i - 1]
        
        line.sort(reverse=True)
        nums.sort(reverse=True)

        return sum(n * l for n, l in zip(line, nums)) % (10**9 + 7)