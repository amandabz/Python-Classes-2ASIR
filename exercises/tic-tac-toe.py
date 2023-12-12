import random

board = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"]
]

board_positions_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]


def print_board():
    for row in board:
        print("|", " | ".join(row), "|")


def draw_game():
    if all(position not in board_positions_list for row in board for position in row):
        return True
    return False


def check_winner(current_player):
    if (
        # check rows
        board[0][0] == current_player and board[0][1] == current_player and board[0][2] == current_player or
        board[1][0] == current_player and board[1][1] == current_player and board[1][2] == current_player or
        board[2][0] == current_player and board[2][1] == current_player and board[2][2] == current_player or

        # check diagonals
        board[0][0] == current_player and board[1][1] == current_player and board[2][2] == current_player or
        board[0][2] == current_player and board[1][1] == current_player and board[2][0] == current_player or

        # check columns
        board[0][0] == current_player and board[1][0] == current_player and board[2][0] == current_player or
        board[0][1] == current_player and board[1][1] == current_player and board[2][1] == current_player or
        board[0][2] == current_player and board[1][2] == current_player and board[2][2] == current_player
    ):
        return True
    return False


def computer_move():
    available_positions = [(index, j) for index, row in enumerate(board)
                           for j, position in enumerate(row) if position in board_positions_list]

    if available_positions:
        return random.choice(available_positions)
    return None


def main():
    current_player = "X"

    while True:
        print_board()

        if current_player == "X":
            print("Computer's move:")
            computer_position = computer_move()

            if computer_position:
                row, col = computer_position
                board[row][col] = "X"

                if check_winner("X"):
                    print_board()
                    print("Player with X icon wins!")
                    break

                elif draw_game():
                    print_board()
                    print("We have a draw!")
                    break

                current_player = "O"

        else:
            try:
                movement = int(input(f"Player O, enter a position (0-9): "))

                if movement <= 9:
                    movement -= 1  # adjustment to start the table index from the number 1
                    row = movement // 3
                    col = movement % 3

                    if board[row][col] in board_positions_list:
                        board[row][col] = "O"

                        if check_winner("O"):
                            print_board()
                            print("Player with O icon wins!")
                            break

                        elif draw_game():
                            print_board()
                            print("We have a draw!")
                            break

                    else:
                        print("Cell already taken or invalid. Try again.")
                        continue

                    current_player = "X" if current_player == "O" else "O"

                else:
                    print("Please enter a value between 1 and 9")
                    continue

            except ValueError:
                print("Please, enter a number between 1 and 9")


if __name__ == "__main__":
    main()
