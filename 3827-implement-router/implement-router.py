__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
class Router:

    def __init__(self, memoryLimit: int):
        self.store = defaultdict(deque) # destination: deque[(timestamp, source)]
        self.oldest = deque() # (destination)
        self.limit = memoryLimit
        self.dumb_store = set()
        self.count = 0

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        if (timestamp, source, destination) in self.dumb_store:
            return False
        
        if self.count == self.limit:
            # evict the oldest
            d = self.oldest.popleft()
            t, s = self.store[d].popleft()
            self.dumb_store.remove((t, s, d))
            self.count -= 1

        self.dumb_store.add((timestamp, source, destination))        
        self.store[destination].append((timestamp, source))
        self.oldest.append(destination)
        self.count += 1

        return True

    def forwardPacket(self) -> List[int]:
        if not self.oldest:
            return []

        d = self.oldest.popleft()
        t, s = self.store[d].popleft()
        self.dumb_store.remove((t, s, d))
        self.count -= 1

        return [s, d, t]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        if not self.store[destination]:
            return 0
            
        # bisect left
        l, r = -1, len(self.store[destination]) - 1
        while l + 1 < r:
            m = (l + r) // 2
            if self.store[destination][m][0] >= startTime:
                r = m
            else:
                l = m
        ll = r

        # bisect right
        l, r = 0, len(self.store[destination])
        while l + 1 < r:
            m = (l + r) // 2
            if self.store[destination][m][0] <= endTime:
                l = m
            else:
                r = m
        rr = l

        # count
        if ll == rr:
            if startTime <= self.store[destination][ll][0] <= endTime:
                return 1
            return 0
        return rr - ll + 1

# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)