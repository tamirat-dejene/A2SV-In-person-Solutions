class FrequencyTracker:

    def __init__(self):
        self.container = {}
        self.freqs = {}

    def add(self, number: int) -> None:
        f = self.container.get(number, 0)
        self.container[number] = f + 1
        self.freqs[f + 1] = self.freqs.get(f + 1, 0) + 1

        if f in self.freqs:
            if self.freqs[f] <= 1: del self.freqs[f]
            else: self.freqs[f] -= 1

    def deleteOne(self, number: int) -> None:
        if number in self.container: 
            f = self.container[number]
            if f <= 1:
                del self.container[number]
            else:
                self.container[number] -= 1
                self.freqs[f - 1] = self.freqs.get(f - 1, 0) + 1
            
            self.freqs[f] -= 1
            if self.freqs[f] <= 0: del self.freqs[f]
        
    def hasFrequency(self, frequency: int) -> bool:
        return frequency in self.freqs
        
# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)