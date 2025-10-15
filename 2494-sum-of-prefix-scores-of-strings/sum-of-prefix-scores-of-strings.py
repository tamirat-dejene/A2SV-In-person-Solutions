class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        idx = {word: i for i, word in enumerate(words)}
        scores, trie = {}, {}

        for word in words:
            curr = trie
            for c in word:
                if c not in curr:
                    curr[c] = {}
                curr = curr[c]
            
            if 'cnt' not in curr:
                curr['cnt'] = 0
            curr['cnt'] += 1
            curr['/'] = True # end of word

        def bottom_up_count(nd, nodes):
            cnt = nodes[nd]['cnt'] if 'cnt' in nodes[nd] else 0
            
            for c in nodes[nd]:
                if c != 'cnt' and c != '/':
                    cnt += bottom_up_count(c, nodes[nd])
                
            nodes[nd]['cnt'] = cnt
            return cnt

        # count words suffix
        for c in trie:
            bottom_up_count(c, trie)
        
        def top_down_build(nd, nodes, store, cnt):
            for c in nodes[nd]:
                if c == '/':
                    scores[''.join(store)] = cnt
                elif c != 'cnt':
                    store.append(c)
                    top_down_build(c, nodes[nd], store, cnt + nodes[nd][c]['cnt'])
                    store.pop()
        
        # collect answers
        for nd in trie:
            top_down_build(nd, trie, [nd], trie[nd]['cnt'])
            
        return [scores[word] for word in words]