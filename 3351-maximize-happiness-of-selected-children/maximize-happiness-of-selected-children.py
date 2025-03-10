class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        ans = happiness[0]

        for i in range(1, k):
            curr = happiness[i]
            ans += (curr - i) if curr - i >= 0 else 0
        
        return ans
        