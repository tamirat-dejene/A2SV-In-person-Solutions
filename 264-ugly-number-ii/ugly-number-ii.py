class Solution:
    def __init__(self):
        self.store = set()

        for i in range(31):
            for j in range(20):
                for k in range(14):
                    a, b, c = 2**i, 3**j, 5**k
                    ab, ac, bc, abc = a*b, a*c, b*c, a*b*c
                    self.store.add(a)
                    self.store.add(b)
                    self.store.add(c)

                    if ab <= 2123366400:
                        self.store.add(ab)
                    if ac <= 2123366400:
                        self.store.add(ac)
                    if bc <= 2123366400:
                        self.store.add(bc)
                    if abc <= 2123366400:
                        self.store.add(abc)
            
        self.store = sorted(self.store)

    def nthUglyNumber(self, n: int) -> int:
        return self.store[n - 1]