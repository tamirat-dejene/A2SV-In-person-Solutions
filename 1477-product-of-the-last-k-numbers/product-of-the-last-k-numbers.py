class ProductOfNumbers:

    def __init__(self):
        self.nums = []
        self.pref_prod = []

    def add(self, num: int) -> None:
        self.nums.append(num)
        if num == 0:
            self.pref_prod = []
        else:
            self.pref_prod.append(num if not self.pref_prod else num * self.pref_prod[len(self.pref_prod) - 1])

    def getProduct(self, k: int) -> int:
        if not self.pref_prod:
            return 0
        
        lst_idx = len(self.pref_prod) - 1
        tot_prod = self.pref_prod[lst_idx]
        if k == lst_idx + 1:
            return tot_prod

        return int(tot_prod / self.pref_prod[lst_idx - k] if lst_idx >= k else 0)
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)