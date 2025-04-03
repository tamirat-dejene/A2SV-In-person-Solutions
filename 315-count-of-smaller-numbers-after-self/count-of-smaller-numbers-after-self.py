class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        srtd = []
        ans = []
        
        for num in nums[::-1]:
            idx = bisect_left(srtd, num)

            ans.append(idx)

            srtd[idx:idx] = [num]
        
        return ans[::-1]
        