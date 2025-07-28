from fasthtml.common import *
from game import Controller

app, rt = fast_app(live=True)

def css():
    return Style("""
        body {
            background-image: url('background_images/background.png');
            background-repeat: repeat-x;
            background-position: 300px;
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
        .board-img {
            width: 55%;
            display: block;
            margin: 0 auto;
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
        .piece {
            position: absolute;
            width: 12.5%; /* 100% / 8 squares */
            height: 12.5%;
            transition: all 0.3s ease; /* For smooth animations */
            z-index: 1;
        }
        .board {
            display: grid;
            grid-template-columns: 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr;  /* 8 columns */
            grid-template-rows: 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr;     /* 8 rows */
        }
        """)

def get_pieces(board):
    images = {"WR": "pieces/WRook.png", "BR": "pieces/BRook.png", "WN": "pieces/WKnight.png", "BN": "pieces/BKnight.png", "WB": "pieces/WBishop.png", "BB": "pieces/BBishop.png", "WQ": "pieces/WQueen.png", "BQ": "pieces/BQueen.png", "WK": "pieces/WKing.png", "BK": "pieces/BKing.png"}
    return [Img(images[img.get_letter()], cls=f"piece{i}") for i, img in enumerate(board)]

@rt('/')
def get():
    c = Controller()
    board = c.generate_board()
    pieces = get_pieces(board)
    print(pieces)

    return Titled("BigJam's Chess Engine",
                  css(),
                  Div(
                      Img(src="background_images/board.png", cls="board-img"),
                        *pieces,
                        cls="board",
    ),
                  cls="title",
    )



serve()