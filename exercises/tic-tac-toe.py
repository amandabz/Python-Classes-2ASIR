import random

board = [
    ["0", "1", "2"],
    ["3", "4", "5"],
    ["6", "7", "8"]
]


def draw_game():
    if all(str(num) not in [item for sublist in board for item in sublist] for num in range(9)):
        return True
    return False


def print_board():
    for row in board:
        print("|", " | ".join(row), "|")


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
    available_positions = [num for row in board for num in row if num.isdigit()]

    if available_positions:
        return int(random.choice(available_positions))
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

                    if board[row][col] != "X" and board[row][col] != "O":
                        board[row][col] = "O"

                        # check if the human is the winner
                        if check_winner("O"):
                            print_board()
                            print("Player with O icon wins!")
                            break

                        elif draw_game():
                            print("We have a draw!")
                            break

                    else:
                        print("Cell already taken. Try again.")
                        continue

                    # switch player
                    current_player = "X" if current_player == "O" else "O"

                else:
                    print("Please enter a value between 0 and 8")
                    continue

            except ValueError:
                print("Please, enter a number between 0 and 8")

        else:
            # computer's move
            print("Computer's move:")
            computer_position = computer_move()

            row = computer_position // 3
            col = computer_position % 3
            board[row][col] = "X"

            # check if the computer is the winner
            if check_winner("X"):
                print_board()
                print("Player with X icon wins!")
                break

            elif draw_game():
                print("We have a draw!")
                break

            # switch player
            current_player = "O"


if __name__ == "__main__":
    main()
