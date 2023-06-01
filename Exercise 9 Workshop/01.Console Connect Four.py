from collections import deque


def place_circle():
    row = 0

    while row != ROWS and board[row][player_col] == "0":
        row += 1

    board[row - 1][player_col] = player_symbol

    return row - 1


def check_for_win(row, col):
    for x, y in directions:
        count = 1

        for i in range(1, 4):
            new_row = row + x * i
            new_col = col + y * i

            if not (0 <= new_row < ROWS and 0 <= new_col < COLS):
                break

            if board[new_row][new_col] != player_symbol:
                break

            count += 1

        for i in range(1, 4):
            new_row = row - x * i
            new_col = col - y * i

            if not (0 <= new_row < ROWS and 0 <= new_col < COLS):
                break

            if board[new_row][new_col] != player_symbol:
                break

            count += 1

        if count >= 4:
            return True


ROWS, COLS = 6, 7

board = [["0"] * COLS for row in range(ROWS)]

player_one_symbol = "1"
player_two_symbol = "2"

turns = deque([[1, player_one_symbol], [2, player_two_symbol]])

win = False

directions = (
    (-1, 0),
    (0, -1),
    (-1, -1),
    (-1, 1),
)

while not win:
    [print(f"[ {', '.join(row)} ]") for row in board]

    player_number, player_symbol = turns[0]

    try:
        player_col = int(input(f"Player {player_number}, please chose a column: ")) - 1
    except ValueError:
        print(f"Select a valid number in the range (1-{COLS})")
        continue

    if not 0 <= player_col < COLS:
        print(f"Select a valid number in the range (1-{COLS})")
        continue

    if board[0][player_col] != "0":
        print("No empty spaces on that column!")
        continue

    row = place_circle()
    win = check_for_win(row, player_col)

    turns.rotate()

print(f"Player {turns[1][0]} wins!")
