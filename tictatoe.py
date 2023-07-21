import random


def markerChoice(p1=0, p2=0):
    while p1 not in ['X', 'O']:
        p1 = input("Player one Choose your sign 'X' or 'O':").upper()
        if p1 == 'X':
            p2 = 'O'
        elif p1 == 'O':
            p2 = 'X'
        else:
            print("invalid input")
    return p1, p2


def pos_view():
    print("  7 | 8 | 9  ")
    print(" ---+---+--- ")
    print("  4 | 5 | 6  ")
    print(" ---+---+--- ")
    print("  1 | 2 | 3  ")


def win_case(board, mark):
    return ((board[1] == board[2] == board[3] == mark) or
            (board[4] == board[5] == board[6] == mark) or
            (board[7] == board[8] == board[9] == mark) or
            (board[7] == board[4] == board[1] == mark) or
            (board[2] == board[5] == board[8] == mark) or
            (board[3] == board[6] == board[9] == mark) or
            (board[7] == board[5] == board[3] == mark) or
            (board[9] == board[5] == board[1] == mark))


def tie_case(board):
    for i in range(1, 10):
        if isEmpty(board, i):
            return False
    return True


def isEmpty(board, pos):
    return board[pos] == ' '


def choice(turn):
    pos = None
    if turn == 'p1':

        while pos not in [0,1, 2, 3, 4, 5, 6, 7, 8, 9] or not isEmpty(board, pos):
            try:
                pos = int(input(
                    f"Enter the position  you would like to place the your marker {turn}({p1}):"))
                if pos == 0:
                    break
                elif pos<0 or pos>10 or not isEmpty(board,pos) :
                    raise ValueError
            except ValueError:
                print("Invalid Input/Position Taken")
        return pos

    elif turn == 'p2':
        while pos not in [0,1, 2, 3, 4, 5, 6, 7, 8, 9,] or not isEmpty(board, pos):
            try:
                pos = int(input(
                    f"Enter the position  you would like to place the your marker {turn}({p2}):"))
                if pos == 0:
                    break
                elif pos<0 or pos>10 or not isEmpty(board,pos) :
                    return ValueError
            except ValueError:
                print("Invalid Input/Position Taken")
        return pos


def player_input(board, choice, marker):
    
    if choice == 0:
        return 0
    else:
        board[choice] = marker


def displaybard(board):
    print(f"  {board[7]} | {board[8]} | {board[9]}  ")
    print(f" ---+---+--- ")
    print(f"  {board[4]} | {board[5]} | {board[6]}  ")
    print(f" ---+---+--- ")
    print(f"  {board[1]} | {board[2]} | {board[3]}  ")


def play():
    ans = ''
    while ans not in ['YES', 'Y', 'NO', 'N']:
        ans = input("would you like to continue?").upper()
        if ans in ['YES', 'Y']:
            print("Restarting game.")
            return True
        elif ans in ['NO', 'N']:
            print("Come back again :D")
            return False
        else:
            print("Yes or no?")
            ans = ''


def quit_game(turn):
    opp = None
    if turn == 'p1':
        while opp not in ['YES','Y','NO','N']:
            try:
                opp = input("Would you like to quite as well p2?").upper()
                if opp in ['YES','Y']:
                    return True
                elif opp in ['NO','N']:
                    return False
                else:
                    raise TypeError
            except TypeError: 
                print("Invalid Input.")
    if turn == 'p2':
        while opp not in ['YES','Y','NO','N']:
            try:
                opp = input("Would you like to quite as well p1?").upper()
                if opp in ['YES','Y']:
                    return True
                elif opp in ['NO','N']:
                    return False
                else:
                    raise TypeError
            except TypeError: 
                print("Invalid Input.")

# __main__


print("Welcome to a game of tic tac toe!\n")
print("You may enter '0' at any time to quit the game.\n")
lol = True
inPlay = True
while True:
    board = {1: ' ', 2: ' ', 3: ' ', 4: ' ',
             5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}
    p1, p2 = markerChoice()
    print(f"Player 1 you are {p1}")
    print(f"player 2 you are {p2}")

    turn = random.choice(["p1", "p2"])
    print(f"And the player who gets the first turn is {turn}")

    while inPlay:
        while turn == 'p1':
            displaybard(board)
            print()
            print()
            pos_view()
            position = player_input(board, choice(turn), p1)
            if win_case(board, p1):
                print("Player 1 wins! Thanks for playing!")
                inPlay = False
                break
            elif tie_case(board):
                print("aww dang its a tie. Well Played!")
                inPlay = False
                break
            elif position == 0:
                if quit_game(turn):
                    print("Alright then.")
                    inPlay = False
                    break
                else:
                    print("Sorry couldn't quit")
                    continue
            else:
                turn = 'p2'

        while turn == 'p2':
            displaybard(board)
            print()
            print()
            pos_view()
            position = player_input(board, choice(turn), p2)
            if win_case(board, p2):
                print("Player 2 wins! Thanks for playing!")
                inPlay = False
                break
            elif tie_case(board):
                print("aww dang its a tie. Well Played!")
                inPlay = False
                break
            elif position == 0:
                if quit_game(turn):
                    print("Alright then.")
                    inPlay = False
                    break
                else:
                    print("Sorry couldn't quit")
                    continue
            else:
                turn = 'p1'

    if play():
        inPlay = True
        print('\n\nNew Game starting now')
        print("\n\nQuick reminder you can enter '0' at any time to quit\n")
        continue
    else:
        print("thank you for playing the game see you next time!! :D")
        break
