class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store = defaultdict(list)
        for word in strs:
            store[''.join(sorted(list(word)))].append(word)
        return list(store.values())