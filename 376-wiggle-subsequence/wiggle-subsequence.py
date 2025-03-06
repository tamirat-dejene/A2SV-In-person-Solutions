class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        cnt, cnt, sign = 0, 0, ''

        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                if not sign or sign == '+':
                    sign = '-'
                    cnt += 1
            elif nums[i] > nums[i - 1]:
                if not sign or sign == '-':
                    sign = '+'
                    cnt += 1
        
        return cnt + 1