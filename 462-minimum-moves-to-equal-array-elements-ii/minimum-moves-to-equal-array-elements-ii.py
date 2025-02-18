class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        tot_cost = sum(nums)
        running_cost = 0
        n = len(nums)

        min_cost = float('inf')
        for i, num in enumerate(nums):
            running_cost += num
            pre_cost = (i + 1) * num - running_cost
            pos_cost = tot_cost - running_cost - (n - i - 1) * num
            min_cost = min(min_cost, pre_cost + pos_cost)
        
        return min_cost


        