class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        dq = deque([deck[-1]])

        for i in range(len(deck) - 2, -1, -1):
            card = dq.pop()
            dq.appendleft(card)
            dq.appendleft(deck[i])
        
        return list(dq)