class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        memo, tot = {}, sum(nums)

        def simulate(l, r):
            pos = str(l) + ':' + str(r)

            if l > r: return 0
            if l == r: return nums[l]
            if pos in memo: return memo.get(pos)


            # player1 plays left, then players2's options
            a = simulate(l + 2, r)
            b = simulate(l + 1, r - 1)

            # player1 plays right, then player2's options
            c = simulate(l + 1, r - 1)
            d = simulate(l, r - 2)
            
            score = max(
                nums[l] + min(a, b), 
                nums[r] + min(c, d) 
            )

            memo[pos] = score

            return score

        player1 = simulate(0, len(nums) - 1)

        return player1 >= tot - player1