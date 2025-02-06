class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        players = [i for i in range(1, n + 1)]
        print(players)
        player_to_be_removed = 0

        while len(players)> 1:
            player_to_be_removed = (player_to_be_removed + k - 1) % len(players)
            players.remove(players[player_to_be_removed])
        
        return players[0]
