import time

class TicTacToe:
    def __init__(self):
        self.initialize_game()

    def initialize_game(self):
        self.current_state = [[".",".","."],
                              [".",".","."],
                              [".",".","."]]
        self.player_turn = "X"

    def draw_board(self):
        print("---------")
        for i in range(3):
            for j in range(3):
                print('{}|'.format(self.current_state[i][j]), end=" ")
            print()
            print("---------")


Game = TicTacToe()
Game.draw_board()
