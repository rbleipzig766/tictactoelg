def print_board(board):
    # Print the Tic Tac Toe board
    for row in board:
        print(" | ".join(row))

def check_winner(board):
    # Check if there is a winner in the current board configuration

    # Check horizontal rows
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return True

    # Check vertical columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " " or board[0][2] == board[1][1] == board[2][0] != " ":
        return True

    return False

def is_board_full(board):
    # Check if the board is full (i.e., no empty spaces remaining)
    return all(cell != " " for row in board for cell in row)

def main():
    # Initialize an empty 3x3 Tic Tac Toe board
    board = [[" " for _ in range(3)] for _ in range(3)]

    # Player X starts
    current_player = "X"

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn")

        while True:
            try:
                # Get user input for row and column
                row = int(input("Enter row (0, 1, or 2): "))
                col = int(input("Enter column (0, 1, or 2): "))

                # Validate input: Check if the input is within valid range and the chosen cell is not already occupied
                if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == " ":
                    break
                else:
                    print("Invalid input. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")
            except IndexError:
                print("Invalid input. Please enter a number between 0 and 2.")

        board[row][col] = current_player

        if check_winner(board):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        current_player = "O" if current_player == "X" else "X"

main()

