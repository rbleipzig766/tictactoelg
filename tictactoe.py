def print_board(board):
    for row in board:
        print(" | ".join(row))

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
            # Spieler-Wechsel
            if current_player == "X":
                current_player = "O"
            else:
                current_player = "X"
        else:
            continue

if __name__ == "__main__":
    main()

