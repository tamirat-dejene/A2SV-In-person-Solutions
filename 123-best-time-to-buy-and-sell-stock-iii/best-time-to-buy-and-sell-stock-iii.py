class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        pref_max = [0]
        pref_min = [0]

        for i in range(1, N):
            if prices[i] < prices[pref_min[-1]]:
                pref_min.append(i)
                pref_max.append(i)
            else:
                pref_min.append(pref_min[-1])
                if prices[i] >= prices[pref_max[-1]]:
                    pref_max.append(i)
                else:
                    pref_max.append(pref_max[-1])

        suff_max = [N - 1]
        suff_min = [N - 1]
        profit_suff = [0]

        for i in range(N - 2, -1, -1):

            if prices[i] > prices[suff_max[-1]]:
                profit_suff.append(max(profit_suff[-1], prices[suff_max[-1]] - prices[suff_min[-1]]))
                
                suff_max.append(i)
                suff_min.append(i)
            else:
                suff_max.append(suff_max[-1])
                if prices[i] <= prices[suff_min[-1]]:
                    suff_min.append(i)
                else:
                    suff_min.append(suff_min[-1])
                profit_suff.append(max(profit_suff[-1], prices[suff_max[-1]] - prices[suff_min[-1]]))

        suff_min = suff_min[::-1]
        suff_max = suff_max[::-1]
        profit_suff = profit_suff[::-1] + [0]

        ans = 0
        for i in range(1, N):
            sofar = prices[pref_max[i]] - prices[pref_min[i]]
            comin = profit_suff[i + 1]
            ans = max(ans, sofar + comin)

        return ans