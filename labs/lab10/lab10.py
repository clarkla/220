"""
Name: Luke Clark
lab10.py
"""


def build():
    board = []
    for i in range(1, 10):
        board.append(i)
    return board


def display(board):
    for i in range(3):
        n = i * 3
        print(board[n], board[n+1], board[n+2], sep=" | ")
        if n == 6:
            break
        print("-" * 9)


def place(board, pos, piece):
    if piece == "X" or "O":
        board[pos - 1] = piece


def legal(board, pos):
    if pos in board and board[pos - 1] == pos:
        return True


def is_won(board, piece):
    for i in range(3):
        n = 3 * i
        if board[n] != piece:
            continue
        if board[n+1] != piece:
            continue
        if board[n+2] != piece:
            continue
        return True
    for i in range(3):
        if board[i] != piece:
            continue
        if board[i+3] != piece:
            continue
        if board[i+6] != piece:
            continue
        return True
    if board[2] == piece:
        if board[4] == piece:
            if board[6] == piece:
                return True
    if board[0] == piece:
        if board[4] == piece:
            if board[8] == piece:
                return True


def is_over(board):
    if is_won(board, "X") is True or is_won(board, "O") is True:
        return True
    else:
        for i in range(1, 10):
            if board[i-1] == i:
                return False
        return True


def main():
    board = build()
    display(board)
    player1 = "X"
    print("PLayer One is X's!")
    player2 = "O"
    print("Player Two is O's :(")
    while True:
        if is_over(board) is True:
            break
        else:
            position = int(input("Player one enter position to play: "))
            if legal(board, position) is True:
                place(board, position, player1)
            display(board)
            if is_over(board) is True:
                break
            else:
                position = int(input("Player two enter position to play: "))
                if legal(board, position) is True:
                    place(board, position, player2)
                display(board)
    if is_won(board, player1) is True:
        print("Player one wins!")
    elif is_won(board, player2) is True:
        print("Player two wins! :(")
    else:
        print("Its a tie")


main()
