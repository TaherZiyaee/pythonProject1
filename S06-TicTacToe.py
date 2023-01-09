board = list(range(1, 10))
player, computer = "X", "O"

# Player: X
# Computer: O
print(f"Player: {player}\nComputer: {computer}\n")


# safheye bazi ra chap mikonad. list mazkoor ra be soorate matrixe 3*3 chap mikonad
def print_board():
    for i in board:
        spliter = " " * 4
        if i % 3 == 0:
            spliter = "\n\n"
        print(f"[{i}]", end=spliter)


# Check mikonad ke tamame khaneha por shode ast ya na. dar vaghe check mikonad ke bazi tamam shode ast ya na
# zamani bazi tamam mishavad ke tamame 9 khane az "X" & "O" por shode bashad
def has_empty_space():
    return board.count("X") + board.count("O") != 9

print_board()
# while has_empty_space():
#     print_board()
