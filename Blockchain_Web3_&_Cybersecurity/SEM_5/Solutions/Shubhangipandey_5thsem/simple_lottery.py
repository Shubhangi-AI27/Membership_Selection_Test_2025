import random
import time
import hashlib

class SimpleLottery:
    def __init__(self, manager):
        self.manager = manager         
        self.players = []             
        self.balance = 0.0            

    # Enter lottery by paying 0.01 ETH
    def enter(self, player, amount):
        if amount != 0.01:
            raise ValueError("Entry fee must be exactly 0.01 ETH")
        self.players.append(player)
        self.balance += amount
        print(f"{player} entered the lottery. Current prize pool: {self.balance} ETH")

    # Private method to generate pseudo-random number
    def _random(self):
        data = str(time.time()) + str(len(self.players)) + str(self.balance)
        hash_val = hashlib.sha256(data.encode()).hexdigest()
        return int(hash_val, 16)

    # Pick winner (manager only)
    def pick_winner(self, caller):
        if caller != self.manager:
            raise PermissionError("Only the manager can pick a winner")
        if len(self.players) == 0:
            raise ValueError("No players in the lottery")

        index = self._random() % len(self.players)
        winner = self.players[index]

        print(f"Winner is {winner}! Prize: {self.balance} ETH")

        # Reset state for next round
        self.players = []
        self.balance = 0.0
        return winner
