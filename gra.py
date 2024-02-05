def print_board(board):
    print("\n   0   1   2")
    print("  " + "-" * 11)
    for i, row in enumerate(board):
        print(i, "|", end=" ")
        for col in row:
            print(col + " |", end=" ")
        print("\n  " + "-" * 11)

def check_winner(board):
    # Sprawdź poziome linie
    for row in board:
        if len(set(row)) == 1 and row[0] != ' ':
            return row[0]

    # Sprawdź pionowe linie
    for col in range(len(board[0])):
        if len(set([board[row][col] for row in range(len(board))])) == 1 and board[0][col] != ' ':
            return board[0][col]

    # Sprawdź przekątne
    if len(set([board[i][i] for i in range(len(board))])) == 1 and board[0][0] != ' ':
        return board[0][0]
    if len(set([board[i][len(board)-i-1] for i in range(len(board))])) == 1 and board[0][len(board)-1] != ' ':
        return board[0][len(board)-1]

    return None

def OX():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    winner = None

    def validate_input(row, col):
        if not (0 <= row < 3 and 0 <= col < 3):
            print("Invalid input! Row and column must be between 0 and 2.")
            return False
        elif board[row][col] != ' ':
            print("That spot is already taken! Choose another one.")
            return False
        return True

    print("Witamy w kółko i krzyżyk!")
    while not winner:
        print_board(board)
        print("Player", current_player)
        valid_input = False
        while not valid_input:
            try:
                row = int(input("Enter row (0, 1, or 2): "))
                col = int(input("Enter column (0, 1, or 2): "))
                valid_input = validate_input(row, col)
            except ValueError:
                print("Invalid input! Please enter a number.")

        board[row][col] = current_player
        winner = check_winner(board)
        if winner:
            print_board(board)
            print("Player", winner, "wins!")
            break
        elif all(board[i][j] != ' ' for i in range(3) for j in range(3)):
            print_board(board)
            print("It's a draw!")
            break
        else:
            current_player = 'O' if current_player == 'X' else 'X'

    print("Game Over!")

OX()


