def print_board(board): for row in board: print(" | ".join(row)) print("-" * 9)

def main(): board = [[" " for _ in range(3)] for _ in range(3)] players = ["X", "O"] current_player = 0

while True:
    print_board(board)
    print(f"Player {players[current_player]}'s turn")

    row = int(input("Enter row (0, 1, or 2): "))
    col = int(input("Enter column (0, 1, or 2): "))

    board[row][col] = players[current_player]

    current_player = 1 - current_player

if name == "main": main()