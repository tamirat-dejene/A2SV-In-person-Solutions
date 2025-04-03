class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)
        st = set(nums)

        dup = 0
        for i in range(1, len(nums) + 1):
            if i not in st:
                dup = i
                break

        return [c for c in cnt if cnt.get(c) == 2] + [dup]