import math
import random

class Player:
    def __init__(self, letter):
        # letter is x or o
        self.letter = letter

    #we want all players to get their next move given a game
    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.AvailableMoves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        validSquare = False
        val = None
        while not validSquare:
            square = input(self.letter + '\'s turn. Input move (0-8)')
            try:
                val = int(square)
                if val not in game.AvailableMoves():
                    raise ValueError
                validSquare = True
            except ValueError:
                print('Invalid sqaure. Try again.')
        return val