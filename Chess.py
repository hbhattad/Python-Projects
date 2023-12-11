class ChessGame:
    def __init__(self):
        self.board = [['BR', 'BN', 'BB', 'BQ', 'BK', 'BB', 'BN', 'BR'],
                      ['BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP'],
                      ['--', '--', '--', '--', '--', '--', '--', '--'],
                      ['--', '--', '--', '--', '--', '--', '--', '--'],
                      ['--', '--', '--', '--', '--', '--', '--', '--'],
                      ['--', '--', '--', '--', '--', '--', '--', '--'],
                      ['WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP'],
                      ['WR', 'WN', 'WB', 'WQ', 'WK', 'WB', 'WN', 'WR']]
        self.current_player = 'W'

    def print_board(self):
        for row in self.board:
            print(' '.join(row))

    def get_move(self):
        move = input("Enter your move (e.g. 'a2 a4'): ")
        return move.split()

    def make_move(self, move):
        start_row = int(move[0][1]) - 1
        start_col = ord(move[0][0]) - ord('a')
        end_row = int(move[1][1]) - 1
        end_col = ord(move[1][0]) - ord('a')
        piece = self.board[start_row][start_col]
        self.board[start_row][start_col] = '--'
        self.board[end_row][end_col] = piece
        self.current_player = 'B' if self.current_player == 'W' else 'W'

    def play(self):
        while True:
            self.print_board()
            move = self.get_move()
            self.make_move(move)

game = ChessGame()
game.play()
