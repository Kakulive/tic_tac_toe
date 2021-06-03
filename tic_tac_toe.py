import sys
import random
import time
from os import system, name


def init_board():
    board = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]
    return board


def get_move(coordinate_dict, player):
    row, col = 0, 0
    valid_input = True
    while valid_input:
        user_input = input(
            f"[Player: {player}] - Please input a valid cell starting from A1 to C3 or type 'quit' to exit: ")
        if user_input.lower() == 'quit':
            sys.exit()
        elif user_input.upper() in coordinate_dict:
            row, col = coordinate_dict[user_input.upper()]
            coordinate_dict.pop(user_input.upper())
            break
        else:
            print("Please select a valid cell, the one you have selected was incorrect!")
            print(f"Available cells that are left: {coordinate_dict.keys()}")
    return row, col


def is_winning_row(board, player):
    for i in board:
        if i.count(player) == 2 and i.count(".") == 1:
            return True

    return False


def column_generator(L, player):
    for i in L:
        if i != player:
            col = L.index(i)
            return col


def winning_row(board, player):
    for i in board:
        if i.count(player) == 2:
            row = board.index(i)
            col = column_generator(i, player)
            x = row, col
            return x


def is_winning_col_diag(board, player):
    rowA, rowB, rowC = board
    new_board = rowA + rowB + rowC
    cond1 = (new_board[0] == new_board[3] == player and new_board[6] == ".") or (
                new_board[3] == new_board[6] == player and new_board[0] == ".") or (
                        new_board[0] == new_board[6] == player and new_board[3] == ".")
    cond2 = (new_board[1] == new_board[4] == player and new_board[7] == ".") or (
                new_board[4] == new_board[7] == player and new_board[1] == ".") or (
                        new_board[1] == new_board[7] == player and new_board[4] == ".")
    cond3 = (new_board[2] == new_board[5] == player and new_board[8] == ".") or (
                new_board[5] == new_board[8] == player and new_board[2] == ".") or (
                        new_board[2] == new_board[8] == player and new_board[5] == ".")
    diag1 = (new_board[0] == new_board[4] == player and new_board[8] == ".") or (
                new_board[4] == new_board[8] == player and new_board[0] == ".") or (
                        new_board[0] == new_board[8] == player and new_board[4] == ".")
    diag2 = (new_board[2] == new_board[4] == player and new_board[6] == ".") or (
                new_board[4] == new_board[6] == player and new_board[2] == ".") or (
                        new_board[2] == new_board[6] == player and new_board[4] == ".")
    if cond1 or cond2 or cond3 or diag1 or diag2 == True:
        return True
    else:
        return False


def winning_col_diag(board, player):
    rowA, rowB, rowC = board
    new_board = rowA + rowB + rowC
    coordinate_dict = {"A1": (0, 0), "A2": (0, 1), "A3": (0, 2), "B1": (1, 0), "B2": (1, 1), "B3": (1, 2), "C1": (2, 0),
                       "C2": (2, 1), "C3": (2, 2)}
    cond1 = new_board[0] == new_board[3] == player
    cond2 = new_board[3] == new_board[6] == player
    cond3 = new_board[0] == new_board[6] == player
    cond4 = new_board[1] == new_board[4] == player
    cond5 = new_board[4] == new_board[7] == player
    cond6 = new_board[1] == new_board[7] == player
    cond7 = new_board[2] == new_board[5] == player
    cond8 = new_board[5] == new_board[8] == player
    cond9 = new_board[2] == new_board[8] == player
    diag1 = new_board[0] == new_board[4] == player
    diag2 = new_board[4] == new_board[8] == player
    diag3 = new_board[0] == new_board[8] == player
    diag4 = new_board[2] == new_board[4] == player
    diag5 = new_board[4] == new_board[6] == player
    diag6 = new_board[2] == new_board[6] == player

    if cond1:
        ai_input = "C1"
        row, col = coordinate_dict["C1"]
        return ai_input, row, col
    elif cond2 == True:
        ai_input = "A1"
        row, col = coordinate_dict["A1"]
        return ai_input, row, col
    elif cond3 == True:
        ai_input = "B1"
        row, col = coordinate_dict["B1"]
        return ai_input, row, col
    elif cond4 == True:
        ai_input = "C2"
        row, col = coordinate_dict["C2"]
        return ai_input, row, col
    elif cond5 == True:
        ai_input = "A2"
        row, col = coordinate_dict["A2"]
        return ai_input, row, col
    elif cond6 == True:
        ai_input = "B2"
        row, col = coordinate_dict["B2"]
        return ai_input, row, col
    elif cond7 == True:
        ai_input = "C3"
        row, col = coordinate_dict["C3"]
        return ai_input, row, col
    elif cond8 == True:
        ai_input = "A3"
        row, col = coordinate_dict["A3"]
        return ai_input, row, col
    elif cond9 == True:
        ai_input = "B3"
        row, col = coordinate_dict["B3"]
        return ai_input, row, col
    elif diag1 == True:
        ai_input = "C3"
        row, col = coordinate_dict["C3"]
        return ai_input, row, col
    elif diag2 == True:
        ai_input = "A1"
        row, col = coordinate_dict["A1"]
        return ai_input, row, col
    elif diag3 == True:
        ai_input = "B2"
        row, col = coordinate_dict["B2"]
        return ai_input, row, col
    elif diag4 == True:
        ai_input = "C1"
        row, col = coordinate_dict["C1"]
        return ai_input, row, col
    elif diag5 == True:
        ai_input = "A3"
        row, col = coordinate_dict["A3"]
        return ai_input, row, col
    elif diag6 == True:
        ai_input = "B2"
        row, col = coordinate_dict["B2"]
        return ai_input, row, col


def get_ai_move(board, coordinate_dict, player):
    row, col = 0, 0
    coord_list_keys = list(coordinate_dict.keys())
    coord_list_values = list(coordinate_dict.values())

    if is_winning_row(board, player) == True:
        ai_input_coord = winning_row(board, player)
        coord_position = coord_list_values.index(ai_input_coord)
        ai_input = coord_list_keys[coord_position]
        row, col = ai_input_coord
    elif is_winning_col_diag(board, player) == True:
        ai_input, row, col = winning_col_diag(board, player)
    else:
        ai_input = random.choice(coord_list_keys)
        row, col = coordinate_dict[ai_input]

    coordinate_dict.pop(ai_input)
    print(f"The computer has chosen {ai_input} as his cell!")

    return row, col


def player_switch(player):
    if player == "X":
        player = "0"
    elif player == "0":
        player = "X"
    return player


def mark(player, board, row, col):
    if board[row][col] == ".":
        board[row][col] = player
    else:
        print("This place is already taken, please choose another one!")

    return board


def has_won(board):
    win = {"A1": board[0][0], "A2": board[0][1], "A3": board[0][2], "B1": board[1][0], "B2": board[1][1],
           "B3": board[1][2], "C1": board[2][0], "C2": board[2][1], "C3": board[2][2]}
    if win["A1"] == win["A2"] == win["A3"] != "." or win["B1"] == win["B2"] == win["B3"] != "." or win["C1"] == win[
        "C2"] == win["C3"] != "." or win["A1"] == win["B1"] == win["C1"] != "." or win["A2"] == win["B2"] == win[
        "C2"] != "." or win["A3"] == win["B3"] == win["C3"] != "." or win["A1"] == win["B2"] == win["C3"] != "." or win[
        "A3"] == win["B2"] == win["C1"] != ".":
        return True
    else:
        return False


def is_full(board):
    if "." in board[0] or "." in board[1] or "." in board[2]:
        return False
    else:
        return True


def print_board(board):
    win = {"A1": board[0][0], "A2": board[0][1], "A3": board[0][2], "B1": board[1][0], "B2": board[1][1],
           "B3": board[1][2], "C1": board[2][0], "C2": board[2][1], "C3": board[2][2]}
    print("    1   2   3 ")
    print("A  " + " " + str(win["A1"]) + " " + "|" + " " + str(win["A2"]) + " " + "|" + " " + str(win["A3"] + " "))
    print("   ---+---+---")
    print("B  " + " " + str(win["B1"]) + " " + "|" + " " + str(win["B2"]) + " " + "|" + " " + str(win["B3"] + " "))
    print("   ---+---+---")
    print("C  " + " " + str(win["C1"]) + " " + "|" + " " + str(win["C2"]) + " " + "|" + " " + str(win["C3"] + " "))


def print_result(winner):
    print("Game is over")
    if winner == "X":
        print("X has won!")
    elif winner == "0":
        print("0 has won!")
    else:
        print("It's a tie")


def play_again():
    while True:
        user_input = input("Would you like to play again ('yes' or 'no'): ")
        if user_input.lower() == "yes":
            return True
        elif user_input.lower() == "no":
            sys.exit()
        else:
            print("Please select 'yes' or 'no': ")


def clear():
    if name == 'nt':
        _ = system('cls')


def tictactoe_game_hum_hum():
    board = init_board()
    player = "X"
    coordinate_dict = {"A1": (0, 0), "A2": (0, 1), "A3": (0, 2), "B1": (1, 0), "B2": (1, 1), "B3": (1, 2), "C1": (2, 0),
                       "C2": (2, 1), "C3": (2, 2)}

    while has_won(board) == False and is_full(board) == False:
        print_board(board)
        row, col = get_move(coordinate_dict, player)
        mark(player, board, row, col)
        player = player_switch(player)
        clear()

    player = player_switch(player)
    print_board(board)
    if has_won(board) == False and is_full(board) == True:
        print_result("tie")
    else:
        print_result(player)

    again = play_again()
    if again == True:
        main_menu()


def tictactoe_game_hum_ai():
    board = init_board()
    player = "X"
    coordinate_dict = {"A1": (0, 0), "A2": (0, 1), "A3": (0, 2), "B1": (1, 0), "B2": (1, 1), "B3": (1, 2), "C1": (2, 0),
                       "C2": (2, 1), "C3": (2, 2)}

    while has_won(board) == False and is_full(board) == False:
        print_board(board)
        if player == "X":
            row, col = get_move(coordinate_dict, player)
        else:
            row, col = get_ai_move(board, coordinate_dict, player)
            time.sleep(1)
        mark(player, board, row, col)
        player = player_switch(player)
        clear()

    player = player_switch(player)
    print_board(board)
    if has_won(board) == False and is_full(board) == True:
        print_result("tie")
    else:
        print_result(player)

    again = play_again()
    if again == True:
        main_menu()


def tictactoe_game_ai_hum():
    board = init_board()
    player = "X"
    coordinate_dict = {"A1": (0, 0), "A2": (0, 1), "A3": (0, 2), "B1": (1, 0), "B2": (1, 1), "B3": (1, 2), "C1": (2, 0),
                       "C2": (2, 1), "C3": (2, 2)}

    while has_won(board) == False and is_full(board) == False:
        print_board(board)
        if player == "0":
            row, col = get_move(coordinate_dict, player)
        else:
            row, col = get_ai_move(board, coordinate_dict, player)
            time.sleep(1)
        mark(player, board, row, col)
        player = player_switch(player)
        clear()

    player = player_switch(player)
    print_board(board)
    if has_won(board) == False and is_full(board) == True:
        print_result("tie")
    else:
        print_result(player)

    again = play_again()
    if again == True:
        main_menu()


def tictactoe_game_ai_ai():
    board = init_board()
    player = "X"
    coordinate_dict = {"A1": (0, 0), "A2": (0, 1), "A3": (0, 2), "B1": (1, 0), "B2": (1, 1), "B3": (1, 2), "C1": (2, 0),
                       "C2": (2, 1), "C3": (2, 2)}

    while has_won(board) == False and is_full(board) == False:
        print_board(board)
        row, col = get_ai_move(board, coordinate_dict, player)
        mark(player, board, row, col)
        time.sleep(1)
        player = player_switch(player)
        clear()

    player = player_switch(player)
    print_board(board)
    if has_won(board) == False and is_full(board) == True:
        print_result("tie")
    else:
        print_result(player)


    again = play_again()
    if again == True:
        main_menu()


def main_menu():
    clear()
    while True:
        user_input_mode = input("""
        Select '1' - Human vs Human
        Select '2' - Human vs AI
        Select '3' - AI vs AI
        'quit' - exits the game
        : """)
        clear()
        if user_input_mode.lower() == 'quit':
            sys.exit()

        if user_input_mode == '2':
            user_input_turn = input("""
            SELECT '1' - you go first
            SELECT '2' - you go second 
            """)
            clear()

        if user_input_mode == '1':
            tictactoe_game_hum_hum()
        elif user_input_mode == '2' and user_input_turn == '1':
            tictactoe_game_hum_ai()
        elif user_input_mode == '2' and user_input_turn == '2':
            tictactoe_game_ai_hum()
        elif user_input_mode == '3':
            tictactoe_game_ai_ai()
        else:
            print("Please select a valid input.")


main_menu()
