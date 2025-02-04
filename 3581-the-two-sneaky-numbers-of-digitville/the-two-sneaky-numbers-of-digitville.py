class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)
        res = [k for k in cnt.keys() if cnt[k] == 2]
        return res
        