class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cnt = Counter(words)
        hp = [(-cnt[w], w) for w in cnt]
        heapify(hp)

        res = []
        while k > 0:
            res.append(heappop(hp)[1])
            k -= 1
        
        return res

        