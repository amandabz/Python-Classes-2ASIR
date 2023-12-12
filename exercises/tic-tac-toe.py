import random

board = [
    ["█", "█", "█"],
    ["█", "█", "█"],
    ["█", "█", "█"]
]


def print_board():
    for row in board:
        print("|", " | ".join(row), "|")


def draw_game():
    if all(position != "█" for row in board for position in row):
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
                           for j, position in enumerate(row) if position == "█"]

    if available_positions:
        return random.choice(available_positions)
    return None


def main():
    current_player = "O"

    while True:
        print_board()

        if current_player == "O":
            try:
                movement = int(input(f"Player O, enter a position (0-8): "))

                if movement <= 8:
                    row = movement // 3
                    col = movement % 3

                    if board[row][col] == "█":
                        board[row][col] = "O"

                        if check_winner("O"):
                            print_board()
                            print("Player with O icon wins!")
                            break

                        elif draw_game():
                            print("We have a draw!")
                            break

                    else:
                        print("Cell already taken or invalid. Try again.")
                        continue

                    current_player = "X" if current_player == "O" else "O"

                else:
                    print("Please enter a value between 0 and 8")
                    continue

            except ValueError:
                print("Please, enter a number between 0 and 8")

        else:
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
                    print("We have a draw!")
                    break

                current_player = "O"


if __name__ == "__main__":
    main()
