class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        line_sweep = [0] * (len(s) + 1)

        for shift in shifts:
            l, r, d = shift
            line_sweep[l] += 1 if d == 1 else -1
            line_sweep[r + 1] += -1 if d == 1 else 1

        line_psum = []
        rsum = 0
        for line in line_sweep:
            rsum += line
            line_psum.append(rsum)

        
        nums = [ord(c) - ord('a') for c in s]
        shifted = []
        
        for num, psum in zip(nums, line_psum):
            shifted.append((num + psum) % 26)


        return ''.join([chr(n + ord('a')) for n in shifted])       
        






        