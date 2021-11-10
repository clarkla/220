"""
Name: <your name goes here – first and last>
<ProgramName>.py
"""
from random import choice


def pick_word(file):
    words = []
    for i in file:
        words.append(i.strip("\n"))
    secret_word = choice(words)
    return secret_word


def create_board(secret_word):
    board = []
    for i in range(len(secret_word)):
        board.append("_")
    return board


def guess_letter(guess, guessed_letters, wrong_guesses, turn_count, secret_word):
    if guess in guessed_letters:
        print("Letter already guessed!! D:")
        return False
    elif len(guess) != 1:
        print("You can only guess one letter at a time! D:")
        return False
    if guess in secret_word:
        guessed_letters.append(guess)
    else:
        guessed_letters.append(guess)
        wrong_guesses.append(guess)
        turn_count[0] += 1


def guess_word(guessed_letters, secret_word, board):
    for i in range(len(secret_word)):
        if secret_word[i] in guessed_letters:
            board[i] = secret_word[i]


def is_won(board, secret_word):
    return "".join(board) == secret_word


def display_board(board, wrong_guesses):
    print(board)
    print("Wrong letters: {}".format(wrong_guesses))


def play_game():
    turn_count = [0]
    guessed_letters = []
    wrong_guesses = []
    file = open("wordlist.txt", "r")
    secret_word = pick_word(file)
    board = create_board(secret_word)
    while turn_count[0] < 7:
        display_board(board, wrong_guesses)
        print("\n")
        guess = input("Enter guessed letter: ")
        print("\n")
        guess_letter(guess, guessed_letters, wrong_guesses, turn_count, secret_word)
        guess_word(guessed_letters, secret_word, board)
        if is_won(board, secret_word) is True:
            break
    if is_won(board, secret_word) is True:
        print("Congratulations! The word was: {}".format(secret_word))
    else:
        print("Oh no, you ran out of turns and I hate you!")


def main():
    play_game()


if __name__ == "__main__":
    main()
