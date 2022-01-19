import time
import pygame as pg
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

    def game_mode(self):
        while True:
            try:
                mode = int(input("(1) fuer Einzelspieler (2) fuer Mehrspieler: "))
            except ValueError:
                mode = 0
                print("Input not a Number")
            if mode == 1 or mode == 2:
                break

        return mode


    def keyboard_input(self):
        try:
            px = int(input("Insert a X-Coordinate: "))
            py = int(input("Insert a Y-Coordinate: "))
        except ValueError:
            print("Invalid Input")
            px = 3
            py = 3

        return px, py

    def is_valid(self, px,py):
        if px > 2 or py > 2:
            return False

        if px < 0 or py < 0:
            return False
        
        elif self.current_state[px][py] != ".":
            return False

        else:
            return True

    def is_end(self):
        for i in range(0, 3):
            if (self.current_state[0][i] != "." and
                self.current_state[0][i] == self.current_state[1][i] and
                self.current_state[1][i] == self.current_state[2][i]):
                return self.current_state[0][i]

        for i in range(0, 3):
            if (self.current_state[i] == ["X", "X", "X"]):
                return "X"
            elif (self.current_state[i] == ["O", "O", "O"]):
                return "O"

        if (self.current_state[0][0] != "." and
            self.current_state[0][0] == self.current_state[1][1] and
            self.current_state[0][0] == self.current_state[2][2]):
            return self.current_state[0][0]

        if (self.current_state[0][2] != "." and
            self.current_state[0][2] == self.current_state[1][1] and
            self.current_state[0][2] == self.current_state[2][0]):
            return self.current_state[0][2]

        for i in range(0, 3):
            for j in range(0, 3):
                if (self.current_state[i][j] == "."):
                    return None

        return "."

    def max(self, alpha, beta):
        maxv = -2
        px = None
        py = None

        result = self.is_end()

        if result == "X":
            return (-1, 0, 0)
        elif result == "O":
            return (1, 0, 0)
        elif result == ".":
            return (0, 0, 0)

        for i in range(0, 3):
            for j in range(0, 3):
                if self.current_state[i][j] == ".":
                    self.current_state[i][j] = "O"
                    (m, min_i, min_j) = self.min(alpha, beta)
                    if m > maxv:
                        maxv = m
                        px = i
                        py = j
                    self.current_state[i][j] = "."
                    #alpha-beta-pruning
                    if maxv >= beta:
                        return (maxv, px, py)
                    if maxv > alpha:
                        alpha = maxv
        return (maxv, px, py)


    def min(self, alpha, beta):
        minv = 2
        px = None
        py = None

        result = self.is_end()

        if result == "X":
            return (-1, 0, 0)
        elif result == "O":
            return (1, 0, 0)
        elif result == ".":
            return (0, 0, 0)

        for i in range(0, 3):
            for j in range(0, 3):
                if self.current_state[i][j] == ".":
                    self.current_state[i][j] = "X"
                    (m, max_i, max_j) = self.max(alpha, beta)
                    if m < minv:
                        minv = m
                        qx = i
                        qy = j
                    self.current_state[i][j] = "."
                    #alpha-beta-pruning
                    if minv <= alpha:
                        return (minv, px, py)
                    if minv < beta:
                        beta = minv

        return (minv, px, py)

    def play(self, mode):
        while True:

            self.draw_board()
            self.result = self.is_end()

            if self.result != None:
                if self.result == "X":
                    print("The Winner is X")
                elif self.result == "O":
                    print("The Winner is O")
                elif self.result == ".":
                    print("Its a Tie")

                self.initialize_game()
                return

            if self.player_turn == "X":
                print("X-Player: ")
                while True:

                    px, py = self.keyboard_input()

                    if self.is_valid(px, py):
                        self.current_state[px][py] = "X"
                        self.player_turn = "O"
                        break
                    else:
                        print('Invalid Move, Try Again')

            elif self.player_turn == "O" and mode == 1:                
                print("O-Player makes his move...")
                (m, px, py) = self.max(-2,2)
                self.current_state[px][py] = "O"                
                self.player_turn = "X"

            elif self.player_turn == "O" and mode == 2:
                print("O-Player: ")
                while True:
                    px, py = self.keyboard_input()

                    if self.is_valid(px, py):
                        self.current_state[px][py] = "O"
                        self.player_turn = "X"
                        break
                    else:
                        print('Invalid Move, Try Again')


Game = TicTacToe()

while True:
    mode = Game.game_mode()
    Game.play(mode)
    while True:
        r = input("New Round? (y/n): ")

        if r == "Y" or r == "y":
            break
        elif r == "N" or r == "n":
            exit(0)
        else:
            print("Invalid Input")