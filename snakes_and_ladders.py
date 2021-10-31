"""https://www.codewars.com/kata/snakes-and-ladders-1/train/python"""

JUMPS = {2: 38, 7: 14, 8: 31, 15: 26, 16: 6, 21: 42, 28: 84, 36: 44, 46: 25, 49: 11, 51: 67, 62: 19, 64: 60, 71: 91, 74: 53, 78: 98, 87: 94, 89: 68, 92: 88, 95: 75, 99: 80}

class SnakesLadders():

    def __init__(self):
        self.players = [0,0]
        self.turn = 0


    @staticmethod
    def adjusted(pos):
        if pos > 100: pos = 200 - pos
        return JUMPS.get(pos, pos)


    def play(self, die1, die2):
        if 100 in self.players: return 'Game over!'

        turn = self.turn
        self.players[turn] = pos = self.adjusted(self.players[turn] + die1 + die2)
        self.turn = turn if die1 == die2 else int(not turn)

        return f"Player {turn + 1} Wins!" if pos == 100 else f"Player {turn + 1} is on square {pos}"


game = SnakesLadders()
print(game.play(1,1))
print(game.play(1,5))
print(game.play(6,2))
print(game.play(1,1))
