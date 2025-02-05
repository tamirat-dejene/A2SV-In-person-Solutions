class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_cnt, ans = Counter(chars), 0
        
        for word in words:
            word_cnt, possible = Counter(word), True
            for c in word_cnt:
                if c not in char_cnt or word_cnt[c] > char_cnt[c]:
                    possible = False
                    break
            
            if possible: ans += len(word)
                
        return ans

