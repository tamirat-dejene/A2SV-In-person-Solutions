class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie, binary, ln = {}, [], len(bin(max(nums))[2:])

        for num in nums:
            curr, bn = trie, bin(num)[2:]
            binary.append('0' * (ln - len(bn)) + bn)

            for c in binary[-1]:
                curr = curr.setdefault('1' if c == '0' else '0', {})

        ans = 0
        for num in binary:
            curr, store = trie, []
            for b in num:
                if b in curr:
                    curr = curr[b]
                    store.append('1' if b == '0' else '0')
                else:
                    store.append('1' if '0' in curr else '0')
                    curr = curr['0' if '0' in curr else '1']

            ans = max(int(num, 2) ^ int(''.join(store), 2), ans)

        return ans              

        