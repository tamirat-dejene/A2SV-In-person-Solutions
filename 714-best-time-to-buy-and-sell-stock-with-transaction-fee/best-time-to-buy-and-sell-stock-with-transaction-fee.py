class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        memo = {}

        def dfs(i, sale):
            if i == len(prices):
                return 0
            
            if (i, sale) not in memo:
                opt1, opt2 = 0, 0
                if sale:
                    opt1 = dfs(i + 1, not sale) + prices[i]
                else:
                    opt2 = dfs(i + 1, not sale) - prices[i] - fee

                opt3 = dfs(i + 1, sale)

                memo[(i, sale)] = max(opt1, opt2, opt3)
                # print(opt1, opt2)
            return memo[(i, sale)]
        
        return dfs(0, False)
        # print(memo)
