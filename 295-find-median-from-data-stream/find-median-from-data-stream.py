class MedianFinder:

    def __init__(self):
        # max allowed len diff = 1
        self.store1 = [] # max_heap
        self.store2 = [] # min_heap
        '''
           Allowed len diff of the two list
           0 <= len(store1) - len(store2) <= 1
        '''
        

    def addNum(self, num: int) -> None:
        heappush(self.store1, -num)
        s1, s2 = len(self.store1), len(self.store2)

        if s1 - s2 > 1:
            heappush(self.store2, -heappop(self.store1))
        
        if self.store1 and self.store2 and -self.store1[0] > self.store2[0]:
            keep = -heappop(self.store1)
            heappush(self.store1, -heappop(self.store2))
            heappush(self.store2, keep)
            
        

    def findMedian(self) -> float:
        if len(self.store1) == len(self.store2):
            return (self.store2[0] - self.store1[0]) / 2
        else:
            return -self.store1[0]

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()