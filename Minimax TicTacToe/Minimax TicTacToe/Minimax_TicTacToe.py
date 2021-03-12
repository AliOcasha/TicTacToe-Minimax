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

    def is_valid(self, px,py):
        if px < 0 or px > 2 or py < 0 or py > 2:
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

    def play(self):
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
                while True:
                    px = int(input("Insert a X-Coordinate: "))
                    py = int(input("Insert a Y-Coordinate: "))

                    if self.is_valid(px, py):
                        self.current_state[px][py] = "X"
                        self.player_turn = "O"
                        break
                    else:
                        print('Invalid Move, Try Again')

            elif self.player_turn == "O":
                while True:
                    px = int(input("Insert a X-Coordinate: "))
                    py = int(input("Insert a Y-Coordinate: "))

                    if self.is_valid(px, py):
                        self.current_state[px][py] = "O"
                        self.player_turn = "X"
                        break
                    else:
                        print('Invalid Move, Try Again')
        else:
            print("Fatal Error!!!")


Game = TicTacToe()
Game.play()



