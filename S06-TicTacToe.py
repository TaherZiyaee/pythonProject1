from colorama import Fore, Back

board = list(range(1, 10))
# board = [1, 2, "X", 4, 5, 6, "O", 8, 9]
player, computer = "X", "O"
winners = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

# Player: X
# Computer: O
print(f"Player: {player}\nComputer: {computer}\n")


# safheye bazi ra chap mikonad. list mazkoor ra be soorate matrixe 3*3 chap mikonad
def print_board():
    j = 1
    for i in board:
        spliter = " " * 4
        if j % 3 == 0:
            spliter = "\n\n"
        if i == "X":
            print(Fore.BLUE + f"[{i}]" + Fore.RESET, end=spliter)
        elif i == "O":
            print(Fore.RED + f"[{i}]" + Fore.RESET, end=spliter)
        else:
            print(f"[{i}]", end=spliter)
        j += 1


# Check mikonad ke tamame khaneha por shode ast ya na. dar vaghe check mikonad ke bazi tamam shode ast ya na
# zamani bazi tamam mishavad ke tamame 9 khane az "X" & "O" por shode bashad
def has_empty_space():
    return board.count("X") + board.count("O") != 9

def can_move(brd, mve):
    # in shart barrasi mikonad ke agar meghdare vared shode beyne 1-9 bashad & adad bashad(yani ghabele harkat bashad)
    if mve in range(1, 10) and isinstance(brd[mve - 1], int):
        return True
    return False

def make_move(brd, plyr, mve, undo=False):
    if can_move(brd, mve):
        brd[mve - 1] = plyr
        win = is_winner(brd, plyr)
        if undo:
            brd[mve - 1] = mve
        return True, win
    return False,False


def is_winner(brd, plyr):
    win = True
    for tpl in winners:
        win = True
        for j in tpl:
            if brd[j] != plyr:
                win = False
                break
        if win:
            break
    return win





# print_board()
while has_empty_space():
    print_board()
    move = int(input("Choose your move(1-9): "))
    moved, won = make_move(board, player, move)
    if not moved:
        print("Invalid number! Please try again...")
        continue
    if won:
        print(Fore.GREEN+"Congratulation, You won!"+Fore.RESET)
        print_board()
        break
