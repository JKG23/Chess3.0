class Piece():
    def __init__(self, coords, colour):
        self.coords = coords
        self.colour = colour
        self.letter = "X"

    def get_letter(self):
        return self.letter

    def __add__(self, other):
        self.coords = self.coords[0] + str((int(self.coords[1]) + other) % 8)

    def __mul__(self, other):
        letters = "abcdefgh"
        for i, letter in enumerate(letters):
            if letter == self.coords[0]:
                self.coords = letters[(i + other) % 8] + self.coords[1]

    def __repr__(self):
        return self.letter

class Pawn(Piece):
    def __init__(self, coords, colour):
        super().__init__(coords, colour)
        self.letter = "'P'"

class Knight(Piece):
    def __init__(self, coords, colour):
        super().__init__(coords, colour)
        self.letter = "'N'"

class Bishop(Piece):
    def __init__(self, coords, colour):
        super().__init__(coords, colour)
        self.letter = "'B'"

class Rook(Piece):
    def __init__(self, coords, colour):
        super().__init__(coords, colour)
        self.castling_rights = True
        self.letter = "'R'"

class Queen(Piece):
    def __init__(self, coords, colour):
        super().__init__(coords, colour)
        self.letter = "'Q'"

class King(Piece):
    def __init__(self, coords, colour):
        super().__init__(coords, colour)

        self.castling_rights = True
        self.letter = "'K'"
