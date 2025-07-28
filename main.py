from fasthtml.common import *
from game import Controller
import time

app, rt = fast_app(live=True)

def css(piece_css):
    return Style("""
        body {
            background-image: url('background_images/background.png');
            background-repeat: repeat-x;
            background-position-x: 300px;
            background-size: 150vh auto;
            min-height: 100vh;
        }
        h1 {
            text-align: center;
            color: white;
            font-size: 2.8em;
            background-color: rgba(0, 0, 0, 0.7);
            padding: 10px;
            margin: 0 auto 20px auto;
            border-radius: 10px;
            max-width: 600px;
        }        
        .board-container {
            position: absolute;
            width: 48%;
            display: block;
            top: 10;
            left: 0;
            right: 0;
            bottom: 10;
            margin: auto;
        }
        .board-img {
            width: 100%;
            z-index: 0;
        }
        .board {
            position: absolute;
            top: 0;
            left: 0;
        }
        .image-container {
            position: relative;
            width: 300px;
            height: 200px;
        }
        .overlay {
            position: absolute;
            top: 20px;
            left: 30px;
            z-index: 2;
        }
        .board {
            display: grid;
            grid-template-columns: 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr;  /* 8 columns */
            grid-template-rows: 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr;     /* 8 rows */
        }
        """ + ''.join(piece_css))

def get_pieces(board, piece_positions):
    images = {"WR": "pieces/WRook.png", "BR": "pieces/BRook.png", "WN": "pieces/WKnight.png", "BN": "pieces/BKnight.png", "WB": "pieces/WBishop.png", "BB": "pieces/BBishop.png", "WQ": "pieces/WQueen.png", "BQ": "pieces/BQueen.png", "WK": "pieces/WKing.png", "BK": "pieces/BKing.png", "WP": "pieces/WPawn.png", "BP": "pieces/BPawn.png"}
    pieces = []

    # pieces = [Img(src="pieces/WRook.png", cls="piece00")]
    # piece_css = [".piece" + str(0) + str(0) + """ {
    #                 grid-column: """ + str(2) + """;
    #                 grid-row: """ + str(2) + """;
    #                 justify-self: center;
    #                 align-self: center;
    #                 z-index: 10;
    #             }
    #             """]
    # return pieces, piece_css


    piece_css = []
    for i, row in enumerate(board):
        for j, piece in enumerate(row):
            if piece == ' ':
                continue
            pieces.append(Img(src=images[piece.colour + piece.get_letter()[1]], cls=f"piece{i}{j}"))
            col, row = piece.c2b()
            print(f"{piece} {piece.coords} {(col, row)}")
            piece_css.append(".piece" + str(i) + str(j) + """ {
                grid-column: """ + str(col + 1) + """;
                grid-row: """ + str(row + 1) + """;
                justify-self: center;
                align-self: center;
                z-index: 10;
            }
            """)
    return pieces, piece_css

@rt('/')
def get():
    c = Controller()
    board = c.generate_board()
    pieces, piece_css = get_pieces(board, c.get_piece_positions())

    return Titled("BigJam's Chess Engine",
                  css(piece_css),
                  Div(
                      Div(
                       Img(src="background_images/board.png", cls="board-img"),
                          Div(
                              *pieces,
                              cls="board",
                          ),
                        ),
                      cls="board-container"
                    ),
                cls="title",
                )

serve()