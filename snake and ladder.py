import random

# The board is represented as a dictionary, where the keys are the positions on the board
# and the values are either 0 (no snake/ladder), -a (a snake going down 'a' positions),
# or +b (a ladder going up 'b' positions).
board = {
    1: 38, 
    4: 14, 
    9: 31, 
    21: 42, 
    28: 84, 
    36: 44, 
    51: 67, 
    71: 91, 
    80: 100, 
    17: 7, 
    64: 60, 
    87: 24, 
    93: 73, 
    95: 75, 
    99: 78
}

# The player starts at position 1.
position = 1

# The player rolls the dice and moves forward the number of steps given by the dice roll.
def move_player(position):
    roll = random.randint(1, 6)
    print(f"You rolled a {roll}.")
    position += roll
    print(f"You are now on square {position}.")
    return position

# If the player lands on a square with a snake or ladder, they move to the new position given by the snake/ladder.
def check_square(position):
    if position in board:
        print("You landed on a square with a snake/ladder.")
        position += board[position]
        print(f"You are now on square {position}.")
    return position

# The game continues until the player reaches square 100.
while position < 100:
    position = move_player(position)
    position = check_square(position)

# The player wins when they reach square 100.
print("You win!")
