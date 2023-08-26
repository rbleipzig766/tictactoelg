# tictactoelg
Context:
Tic Tac Toe is a classic two-player game played on a 3x3 surface. Each player takes turns marking a cell with their symbol (either 'X' or 'O'). The winner is the person who is the first to form a horizontal, vertical, or diagonal line of three of your symbols.
Why is it interesting?
It´s one of the most known games and it´s quite simple to play. The instructions for the code could serve a fundamental exercise in programming, helping me to understand basic concepts. While the game itself is simple, implementing a playable version involves handling user interactions, checking for win conditions, and ensuring a smooth flow of gameplay.

Algorithm:

    Initialize the Game:
        Create a 3x3 surface
        ask the users who is going to start first (X or O)

    Game Loop:
        Repeat the following steps until the game is over:
            Show all the moves taken from both players on the surface
            Ask the current player for his move 
            The field needs to be empty
            Show the players symbol on the 3x3 surface
            Switch to the other player.

    The winner is:
        who has three x´s or o´s in a row (rows, columns, and diagonals)

    Draw Condition:
        If the entire surface is filled and no player has won, the game ends in a draw.

    Display Result:
        Display winner or if it´s a draw

    Display winner or if it´s a draw



First delivery:

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = 0

    while True:
        print_board(board)
        print(f"Player {players[current_player]}'s turn")

        row = int(input("Enter row (0, 1, or 2): "))
        col = int(input("Enter column (0, 1, or 2): "))

        board[row][col] = players[current_player]

        current_player = 1 - current_player

if __name__ == "__main__":
    main()
