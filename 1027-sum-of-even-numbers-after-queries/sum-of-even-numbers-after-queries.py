class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even_sum, ans = sum([n for n in nums if n % 2 == 0]), []
        for add, index in queries:
            if (nums[index] + add) % 2 == 0:
                if nums[index] % 2 == 0:
                    even_sum += add
                else:
                    even_sum += nums[index] + add
            else:
                if nums[index] % 2 == 0:
                    even_sum -= nums[index]
            ans.append(even_sum)
            nums[index] += add
        
        return ans
        