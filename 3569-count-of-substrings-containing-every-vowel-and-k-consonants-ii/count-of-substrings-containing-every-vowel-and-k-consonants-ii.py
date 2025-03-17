class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        V = {'a', 'e', 'i', 'o', 'u'}
        
        l, nl = 0, 0 # left, near left
        vowels = defaultdict(int)
        vcount, ccount = 0, 0
        
        res = 0

        for r, curr in enumerate(word):
            if curr in V:
                if vowels[curr] == 0: vcount += 1
                vowels[curr] += 1
            else: ccount += 1

            while ccount > k:
                if l < nl: l = nl
                if word[l] in V:
                    vowels[word[l]] -= 1
                    if vowels[word[l]] == 0: 
                        vowels.pop(word[l])
                        vcount -= 1
                else: ccount -= 1
                l += 1 
            
            if vcount == 5 and ccount == k:
                if nl < l: nl = l
                while word[nl] in V and vowels[word[nl]] > 1:
                    vowels[word[nl]] -= 1
                    nl += 1
                res += nl - l + 1

        return res