def print_board(board):
    for row in board:
        print(" | ".join(row))

def check_winner(board):
    # Überprüfe horizontale Reihen
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return True

    # Überprüfe vertikale Reihen
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return True

    # Überprüfe diagonale Reihen
    if board[0][0] == board[1][1] == board[2][2] != " " or board[0][2] == board[1][1] == board[2][0] != " ":
        return True

    return False

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]

    # Spieler-Wechsel (X startet)
    current_player = "X"

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn")

        # Benutzereingabe für den Zug
        row = int(input("Enter row (0, 1, or 2): "))
        col = int(input("Enter column (0, 1, or 2): "))

        # Überprüfung, ob das Feld bereits belegt ist
        if board[row][col] == " ":
            board[row][col] = current_player
            
            # Überprüfe, ob jemand gewonnen hat
            if check_winner(board):
                print_board(board)
                print(f"Player {current_player} wins!")
                break
            
            # Spieler-Wechsel
            if current_player == "X":
                current_player = "O"
            else:
                current_player = "X"
        else:
            continue

if __name__ == "__main__":
    main()


