class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        # asssume the last to be the first character
        i, N = 0, len(bits)

        while i < N:
            i += 1 + (bits[i] == 1)
            if i == N - 1:
                return True
        
        return N == 1