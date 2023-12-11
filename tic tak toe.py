# The board is represented as a 2D list of size 3x3, where each cell is either 'X', 'O', or ' '.
board = [[' ' for x in range(3)] for y in range(3)]

# The players take turns placing their symbol on the board.
def play_turn(board, symbol, row, col):
    if row >= 0 and row <= 2 and col >= 0 and col <= 2 and board[row][col] == ' ':
        board[row][col] = symbol
    else:
        print("Invalid move, try again.")

# Check if a player has won by having 3 symbols in a row, column, or diagonal.
def check_win(board, symbol):
    for i in range(3):
        if board[i][0] == symbol and board[i][1] == symbol and board[i][2] == symbol:
            return True
        if board[0][i] == symbol and board[1][i] == symbol and board[2][i] == symbol:
            return True
    if board[0][0] == symbol and board[1][1] == symbol and board[2][2] == symbol:
        return True
    if board[0][2] == symbol and board[1][1] == symbol and board[2][0] == symbol:
        return True
    return False

# The game continues until either player X or O wins or all cells are filled with symbols.
turn = 'X'
while True:
    print(f'Turn of player {turn}:')
    row = int(input('Enter row number (0-2): '))
    col = int(input('Enter column number (0-2): '))
    play_turn(board, turn, row, col)
    if check_win(board, turn):
        print(f'Player {turn} wins!')
        break
    full = True
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                full = False
                break
        if not full:
            break
    if full:
        print('The game is a draw.')
        break
    turn = 'X' if turn == 'O' else 'O'

# Print the final state of the board.
print('Final state of the board:')
for i in range(3):
    print(board[i])
