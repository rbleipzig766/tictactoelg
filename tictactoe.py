"""
Final project for computational thinking for engeneering

Programming the famous game tic tac toe:
Two players can take turns placing their markers on a 3x3 square. The first player to have 3 of his markers
in a row, column or diagonal wins. If the field is full without a winner, it is a draw.

Name: Luca Gransow A01762583
Date: 15.10.2023
"""


"""
Function print_board: Prints the game board.

    Input:
    - board (list): A 2D list representing the game board.

    Process:
    - Iterates through the board and prints rows and separators.

    Output:
    - None
"""

def print_board(board):
    for row in board:
        print(" | ".join(row)) 
        print("-" * 10)
        
"""
Function check_winner: Checks if there is a winner.

    Input:
    - board (list): A 2D list representing the game board.

    Process:
    - Checks rows, columns, and diagonals for winning combinations (if there is the same symbole three times in a line, there is a winner)

    Output:
    - True if there is a winner, otherwise False.
"""        

def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return True

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return True

    if board[0][0] == board[1][1] == board[2][2] != " " or board[0][2] == board[1][1] == board[2][0] != " ":
        return True

    return False


"""
Function is_board_full: Checks if the board is full.

    Input:
    - board (list): A 2D list representing the game board.

    Process:
    - Checks if every cell in the board is occupied.

    Output:
    - True if the board is full, otherwise False.
"""

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

"""
Function save_game: Saves the game state to a file.

    Input:
    - player_scores: A dictionary containing player scores.

    Process:
    - Opens a file and writes player scores in the file format.

    Output:
    - None (changed text in text file)
"""

def save_game(player_scores):
    with open('spielstand.txt', 'w') as file:
        for player, score in player_scores.items():
            file.write(f"{player}:{score}\n")
            
"""
Function load_game: Loads the game state from a file.

    Input:
    - None

    Process:
    - Read the game state from a file.

    Output:
    - player_scores: A dictionary containing player scores.
"""


def load_game():
    player_scores = {'X': 0, 'O': 0, 'Tie': 0}
    try:
        with open('spielstand.txt', 'r') as file:
            for line in file:
                parts = line.strip().split(':')
                if len(parts) == 2:
                    player, score = parts
                    if player != 'Tie':
                        player_scores[player] = int(score)
    except FileNotFoundError:
        pass
    return player_scores

def menu():
    print("\n1. Start New Game\n2. Quit")
    choice = input("Enter your choice (1 or 2): ")
    return choice

def main():
    # Load player scores from file 
    player_scores = load_game()

    while True:
        # Display menu and receive user's choice
        choice = menu()

        if choice == "1":
            # Initialize empty board and set the current player to "X"
            board = [[" " for i in range(3)] for i in range(3)]
            current_player = "X"

            while True:
                print_board(board)  # Print board
                print(f"Player {current_player}'s turn")

                while True:
                    try:
                        row = int(input("Enter row (0, 1, or 2): "))  # Get user input for row
                        col = int(input("Enter column (0, 1, or 2): "))  # Get user input for column

                        # Check if input is valid 
                        if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == " ":
                            break
                        else:
                            print("Invalid input. Please try again.")
                    except ValueError:
                        print("Invalid input. Please enter a number.")
                    except IndexError:
                        print("Invalid input. Please enter a number between 0 and 2.")

                board[row][col] = current_player  # Update the board with the current player's move

                # Check if the current player has won
                if check_winner(board):
                    print_board(board)
                    print(f"Player {current_player} wins!")
                    player_scores[current_player] += 1  # Update player's score
                    break

                # Check if board is full (tie)
                if is_board_full(board):
                    print_board(board)
                    print("It's a tie!")
                    player_scores['Tie'] += 1  # Update tie score
                    break

                current_player = "O" if current_player == "X" else "X"  # Switch players

            print("Current Scores:")
            for player, score in player_scores.items():
                if player != 'Tie':
                    print(f"Player {player}: {score} wins")
            print(f"Ties: {player_scores['Tie']}")  

            # Save the updated scores to file
            save_game(player_scores)

        elif choice == "2":
            # Display final scores
            print("Final Scores:")
            for player, score in player_scores.items():
                if player != 'Tie':
                    print(f"Player {player}: {score} wins")
            print(f"Ties: {player_scores['Tie']}")  
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

main()

