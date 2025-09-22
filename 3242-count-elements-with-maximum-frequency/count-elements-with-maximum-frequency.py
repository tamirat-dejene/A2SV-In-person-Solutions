class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        tmp = list(Counter(nums).values())
        mf = max(tmp)
        return tmp.count(mf) * mf