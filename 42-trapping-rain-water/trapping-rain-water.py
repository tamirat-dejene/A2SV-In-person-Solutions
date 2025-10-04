class Solution:
    def trap(self, height: List[int]) -> int:
        N = len(height)
        if N <= 2: return 0
            
        tall_pref = [0]
        tall_suff = [N - 1]

        for i in range(1, N):
            if height[i] > height[tall_pref[-1]]:
                tall_pref.append(i)
            else:
                tall_pref.append(tall_pref[-1])

        for i in range(N - 2, -1, -1):
            if height[i] > height[tall_suff[-1]]:
                tall_suff.append(i)
            else:
                tall_suff.append(tall_suff[-1])
        tall_suff = tall_suff[::-1]

        tallest = height.index(max(height))
        ans = 0

        # Go left
        tl = tallest
        while tl > 1:
            nt = tall_pref[tl - 1]

            ans += (tl - nt) * height[nt] - sum(height[i] for i in range(nt, tl))
            tl = nt

        # Go right
        tr = tallest
        while tr < N - 2:
            nt = tall_suff[tr + 1]

            ans += (nt - tr) * height[nt] - sum(height[i] for i in range(tr + 1, nt + 1))
            tr = nt
        
        return ans







        
        


    