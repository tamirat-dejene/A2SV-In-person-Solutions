class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        nums, ln = list(map(lambda n: -n, nums)), len(nums)
        heapify(nums)

        self.mx_heap = nums
        self.mn_heap = []

        while len(self.mx_heap) > ln - k + 1:
            heappush(self.mn_heap, -heappop(self.mx_heap))
        
    def add(self, val: int) -> int:
        if (self.mx_heap and val >= -self.mx_heap[0]) or (self.mn_heap and val >= self.mn_heap[0]):
            heappush(self.mn_heap, val)
            heappush(self.mx_heap, -heappop(self.mn_heap))
        else:
            heappush(self.mx_heap, -val)

        return -self.mx_heap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)