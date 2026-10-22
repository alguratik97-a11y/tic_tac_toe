
board = [" " for _ in range(10)]

def print_board():
    print("   |   |   ")
    print(f" {board[1]} | {board[2]} | {board[3]} ")
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(f" {board[4]} | {board[5]} | {board[6]} ")
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(f" {board[7]} | {board[8]} | {board[9]} ")
    print("   |   |   ")

def is_board_full(board):
    return board.count(' ') == 1

def check_win(board, letter):
    return ((board[1] == letter and board[2] == letter and board[3] == letter) or
            (board[4] == letter and board[5] == letter and board[6] == letter) or
            (board[7] == letter and board[8] == letter and board[9] == letter) or
            (board[1] == letter and board[4] == letter and board[7] == letter) or
            (board[2] == letter and board[5] == letter and board[8] == letter) or
            (board[3] == letter and board[6] == letter and board[9] == letter) or
            (board[1] == letter and board[5] == letter and board[9] == letter) or
            (board[3] == letter and board[5] == letter and board[7] == letter))

def player_move(letter):
    run = True
    while run:
        move = input(f"Select position for '{letter}' (1-9): ")
        try:
            move = int(move)
            if 1 <= move <= 9:
                if board[move] == ' ':
                    board[move] = letter
                    run = False
                else:
                    print('This space is already occupied!')
            else:
                print('Please type a number within the range (1-9)!')
        except ValueError:
            print('Please type a valid number!')

def main():
    print("Welcome to Tic Tac Toe!")
    print_board()

    while not is_board_full(board):
        if not check_win(board, 'O'):
            player_move('X')
            print_board()
            if check_win(board, 'X'):
                print("X wins! Congratulations!")
                break
        else:
            print("O wins! Congratulations!")
            break

        if not check_win(board, 'X'):
            player_move('O')
            print_board()
            if check_win(board, 'O'):
                print("O wins! Congratulations!")
                break
        else:
            print("X wins! Congratulations!")
            break

    if is_board_full(board):
        print("Tie Game!")

if __name__ == "__main__":
    main()
