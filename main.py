# print the current iteration of the board
def print_board(matrix):
    for i, row in enumerate(matrix):
        ## updating the layout of the positions here instead of the actual matrix itself 
        print("  |  ".join(cell.ljust(3) for cell in row))
        if i < len(matrix) - 1:
            print("-----|-------|-----")

# update the board based on user input
def update_board(new_pos, player, matrix):
    positions = {
        "A1": (0, 0), "B1": (0, 1), "C1": (0, 2),
        "A2": (1, 0), "B2": (1, 1), "C2": (1, 2),
        "A3": (2, 0), "B3": (2, 1), "C3": (2, 2)
    }

    if positions[new_pos] != "X" and positions[new_pos] != "O":
        row, col = positions[new_pos]
        if new_pos[0] == "A":
            matrix[row][col] = player
        elif new_pos[0] == "B":
            matrix[row][col] = player
        elif new_pos[0] == "C":
            matrix[row][col] = player
    else:
        print("This position is already taken. Please choose a different position.")

# Check for a winner by looking at each of the winning circumstances
def check_winner(matrix):
    ## check rows
    for row in range(3):
        if matrix[row][0] == matrix[row][1] == matrix[row][2] and matrix[row][0] in ["X", "O"]:
            return matrix[row][0]
    ## check columns
    for col in range(3):
        if matrix[0][col] == matrix[1][col] == matrix[2][col] and matrix[0][col] in ["X", "O"]:
            return matrix[0][col]
   ## check right to left diagonal
    if matrix[0][0] == matrix[1][1] == matrix[2][2] and matrix[0][0] in ["X", "O"]:
        return matrix[0][0]
    ## check left to right diaganol
    if matrix[0][2] == matrix[1][1] == matrix[2][0] and matrix[0][2] in ["X", "O"]:
        return matrix[0][2]
    return None

# Main game loop
play_matrix = [
    ["A1", "B1", "C1"],
    ["A2", "B2", "C2"],
    ["A3", "B3", "C3"]
]

print("Welcome to the Tic Tac Toeinator 666")

proceed = input("Type 'y' to continue: ").upper()
if proceed == "Y":
    print("The first player is 'X")
    print_board(play_matrix)
    current_player = "X"

    while True:
        user_input = input(f"Player {current_player}, please choose your space (or type 'QUIT' to exit): ").upper()
        if user_input == "QUIT":
            print("Game over")
            break
        
        if len(user_input) != 2 or user_input[0] not in "ABC" or user_input[1] not in "123":
            print("Invalid input. Please enter a valid position (A1, B2).")
            continue
        
        update_board(user_input, current_player, play_matrix)
        winner = check_winner(play_matrix)
        print_board(play_matrix)
        if winner:
            print(f"The winner is {winner}!")
            break
        current_player = "O" if current_player == "X" else "X"
