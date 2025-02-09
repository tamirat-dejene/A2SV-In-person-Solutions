class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        '''
        i < j and 
        j - i != nums[j] - nums[i]
        nums[i] - i != nums[j] - j

        count those pairs that equals and subtract them from the total possible number of pairs
        '''

        num_idx_diff_cnt = defaultdict(int)
        for i, num in enumerate(nums): num_idx_diff_cnt[num - i] += 1
        
        equal_pairs = sum([c * (c - 1) // 2 for c in num_idx_diff_cnt.values()])
        tot_pairs = len(nums) * (len(nums) - 1) // 2

        return tot_pairs - equal_pairs
        

        