class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = {}
        for word in dictionary:
            curr = trie
            for c in word:
                if c not in curr:
                    curr[c] = {}
                curr = curr[c]
            curr['/'] = True
        
        ans = []

        for word in sentence.split():
            curr = trie

            pref = []

            for c in word:
                if c not in curr:
                    if '/' not in curr:
                        pref = []
                    break
                
                pref.append(c)
                curr = curr[c]

                if '/' in curr:
                    break

            if not pref:
                ans.append(word)
            else:
                ans.append(''.join(pref))
            
        return ' '.join(ans) 
