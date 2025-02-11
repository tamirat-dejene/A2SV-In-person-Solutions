class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def bubble_sort(lst, key):
            s = len(lst)
            while True:
                swapped = False
                for i in range(1, s):
                    if not key(lst[i - 1], lst[i]):
                        lst[i], lst[i - 1] = lst[i - 1], lst[i]
                        swapped =True
                if not swapped: break
                s -= 1
            return lst

        string = ''.join(bubble_sort(list(map(str, nums)), key=lambda item1, item2: item2 + item1 < item1 + item2))

        return string if string.lstrip('0') else '0'
        