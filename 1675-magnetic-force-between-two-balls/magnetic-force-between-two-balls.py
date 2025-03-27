class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        size = len(position)
        
        def check(force):
            cnt, l = 1, position[0]
            
            while True:
                nxt = l + force
                idx = bisect.bisect_left(position, nxt)
                
                if idx >= size: return cnt >= m
                
                cnt += 1
                l = position[idx]
                
                if cnt == m: return True
        
        left, right = 1, position[-1] - position[0]
        result = 0
        
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                result = mid
                left = mid + 1
            else:
                right = mid - 1
                
        return result