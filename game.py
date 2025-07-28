from pieces import *


class Controller:
    def __init__(self):
        self._piece_positions = {}
        self.generate_board()

    def generate_board(self):
        self.board = [[' '] * 8 for _ in range(8)]

        # Black Pieces
        self.board[0][0] = Rook("h1", colour="B")
        self.board[0][1] = Knight("h2", colour="B")
        self.board[0][2] = Bishop("h3", colour="B")
        self.board[0][3] = Queen("h4", colour="B")
        self.board[0][4] = King("h5", colour="B")
        self.board[0][5] = Bishop("h6", colour="B")
        self.board[0][6] = Knight("h7", colour="B")
        self.board[0][7] = Rook("h8", colour="B")

        self._piece_positions["BR"] = ["a8", "h8"]
        self._piece_positions["BN"] = ["b8", "g8"]
        self._piece_positions["BB"] = ["c8", "f8"]
        self._piece_positions["BQ"] = ["d8"]
        self._piece_positions["BK"] = ["e8"]

        # White Pieces
        self.board[7][0] = Rook("a1", colour="W")
        self.board[7][1] = Knight("a2", colour="W")
        self.board[7][2] = Bishop("a3", colour="W")
        self.board[7][3] = Queen("a4", colour="W")
        self.board[7][4] = King("a5", colour="W")
        self.board[7][5] = Bishop("a6", colour="W")
        self.board[7][6] = Knight("a7", colour="W")
        self.board[7][7] = Rook("a8", colour="W")

        self._piece_positions["WR"] = ["a1", "h1"]
        self._piece_positions["WN"] = ["b1", "g1"]
        self._piece_positions["WB"] = ["c1", "f1"]
        self._piece_positions["WQ"] = ["d1"]
        self._piece_positions["WK"] = ["e1"]

        # Black Pawns
        for i in range(8):
            self.board[6][i] = Pawn("g" + str(i), colour="B")
            self._piece_positions["BP"] = ["g" + str(i)]

        # White Pawns
        for i in range(8):
            self.board[1][i] = Pawn("b" + str(i), colour="W")
            self._piece_positions["WP"] = ["b" + str(i)]

        self.show()
        [print(i, val) for i, val in self._piece_positions.items()]

        return self.board

    def show(self):
        [print(i) for i in self.board]


def main():
    c = Controller()

if __name__ == "__main__":
    main()