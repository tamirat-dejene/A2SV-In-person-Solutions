class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ln = len(nums)
        st = set()
        
        for i in range(len(nums)):
            while nums[i] != i + 1:
                if nums[nums[i] - 1] == nums[i]: 
                    st.add(nums[i])
                    break
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
            
        return list(st)