class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        pref = [0]

        for num in arr:
            pref.append(num ^ pref[-1])
        
        return [pref[r + 1] ^ pref[l] for l, r in queries]
        