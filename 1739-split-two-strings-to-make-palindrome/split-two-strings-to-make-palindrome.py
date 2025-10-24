class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        N = len(a)

        # a: prefix, b: suffix
        la, rb = 0, N - 1
        while la < rb and a[la] == b[rb]:
            la += 1
            rb -= 1
        
        aa = b[la:rb+1]
        bb = a[la:rb+1]

        if aa == aa[::-1] or bb == bb[::-1]:
            return True

        lb, ra = 0, N - 1
        while lb < ra and b[lb] == a[ra]:
            lb += 1
            ra -= 1

        aa = a[lb:ra+1]
        bb = b[lb:ra+1]

        return aa == aa[::-1]or bb == bb[::-1]