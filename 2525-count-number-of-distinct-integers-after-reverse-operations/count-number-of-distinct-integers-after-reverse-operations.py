class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        nums = set(nums)
        tmp = set()
        for n in nums:
            tmp.add(int(str(n)[::-1]))
        
        for t in tmp: nums.add(t)
        return len(nums)
        
        