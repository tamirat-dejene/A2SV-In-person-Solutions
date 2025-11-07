class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        psum = list(accumulate(stations))
        N = len(stations)
        power = []

        for i in range(N):
            rr = psum[min(i + r, N - 1)]
            ll = psum[i - r - 1] if i - r - 1 >= 0 else 0
            power.append(rr - ll)
        
        def can_power(pw):
            added, kc = [0] * (N + 1), k

            for city in range(N - 1, -1, -1):
                added[city] += added[city + 1]
                
                if added[city] + power[city] < pw:

                    req = pw - power[city] - added[city]
                    if req > kc: return False

                    added[city] += req
                    if city - 2 * r - 1 >= 0:
                        added[city - 2 * r - 1] -= req

                    kc -= req

            return True

        l1, r1 = min(power), max(power) + k + 1

        while l1 + 1 < r1:
            m = (l1 + r1) // 2

            if can_power(m):
                l1 = m
            else:
                r1 = m

        return l1