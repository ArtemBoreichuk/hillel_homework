import random


class ChessBoard:
    def __init__(self):
        self.board = [[' ' for _ in range(8)] for _ in range(8)]

    def place_random_pieces(self):
        pieces = ['♚', '♛', '♜', '♝', '♞', '♟']
        random.shuffle(pieces)

        # Place white king and black king
        self.board[0][4] = pieces[0]
        self.board[7][4] = pieces[1]

        # Place other random pieces
        for piece in pieces[2:]:
            row, col = random.randint(0, 7), random.randint(0, 7)
            while self.board[row][col] != ' ':
                row, col = random.randint(0, 7), random.randint(0, 7)
            self.board[row][col] = piece

    def print_board(self):
        print('  A B C D E F G H')
        print(' ┌─────────────────┐')
        for i, row in enumerate(self.board):
            print(f'{8 - i}│', end=' ')
            for col in row:
                print(col, end=' ')
            print('│', 8 - i)
        print(' └─────────────────┘')
        print('  A B C D E F G H')


chess_board = ChessBoard()
chess_board.place_random_pieces()
chess_board.print_board()
for _ in range(2):
    print('\n' + '-' * 25 + '\n')
    chess_board = ChessBoard()
    chess_board.place_random_pieces()
    chess_board.print_board()
