import math
import time
from player import HumanPlayer, RandomComputerPlayer


class TicTacToe:
    def __init__(self):
        self.board = self.MakeBoard() # we will use a single list to rep 3x3 board
        self.currentWinner = None # keep track of winner

    @staticmethod
    def MakeBoard():
        return [' ' for _ in range(9)]
    
    def PrintBoard(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('|' + '|'.join(row) + '|')

    @staticmethod
    def PrintBoardNums():
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('|' + '|'.join(row) + '|')

    def AvailableMoves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def EmptySquares(self):
        return ' ' in self.board

    def NumEmptySquares(self):
        return self.board.count('')

    def MakeMove(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.currentWinner = letter
            return True
        else:
            return False

    def winner(self, square, letter):
        rowInd = square // 3
        row = self.board[rowInd*3 : (rowInd + 1) * 3]
        if all([spot == letter for spot in row]):
            return True
        
        colInd = square % 3
        column = [self.board[colInd+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True

        return False

def play(game, x_player, o_player, printGame=True):
    if printGame:
        game.PrintBoardNums()
    
    letter = 'X' #starting letter

    while game.EmptySquares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
    
        if game.MakeMove(square, letter):
            if printGame:
                print(letter + f' makes a move to square {square}')
                game.PrintBoard()
                print('')

            if game.currentWinner:
                if printGame:
                    print(letter + "wins!")
                return letter

            letter = 'O' if letter == 'X' else 'X'

        time.sleep(0.08s)

    if printGame:
        print('It\'s a tie!')

if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, printGame=True)
