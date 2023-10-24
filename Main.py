# tic tac toe game using classes
import os
import re
from weakref import ref

os.system("clear")


class Board:
    def __init__(self):
        # init spaces for board
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

    def display(self):
        print(f" {self.cells[1]} | {self.cells[2]} | {self.cells[3]} ")
        print("-----------")
        print(f" {self.cells[4]} | {self.cells[5]} | {self.cells[6]} ")
        print("-----------")
        print(f" {self.cells[7]} | {self.cells[8]} | {self.cells[9]} ")

    def update_cell(self, cell_num, player):
        self.cells[cell_num] = player

    def is_winner(self, player):
        """checks if player has won"""
        win_conditions = (
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
            [1, 4, 7],
            [2, 5, 8],
            [3, 6, 9],
            [1, 5, 9],
            [3, 5, 7],
        )
        for condition in win_conditions:
            if (
                self.cells[condition[0]] == player
                and self.cells[condition[1]] == player
                and self.cells[condition[2]] == player
            ):
                return True
            else:
                return False

    def is_tie(self):
        """checks if game is a tie"""
        # Check if all the cells in the board are filled
        # by iterating over the cells and checking if they
        # are not equal to " ".
        if all(cell != " " for cell in self.cells[1:9]):
            return True
        else:
            return False

    def reset(self):
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]


board = Board()


def print_header():
    print("Welcome to Tic Tac Toe!\n")


def refresh_screen():
    # clear the screen
    os.system("clear")
    # print the header
    print_header()
    # show the board
    board.display()


while True:
    # x turn
    refresh_screen()

    # get X input and update board
    x_choice = int(input("\nX) Please choose 1-9. > "))
    # check if input is valid
    # check if input is a number between 1-9
    while x_choice not in range(1, 10):
        print("\nSorry, that is not a valid choice.\n")
        x_choice = int(input("\nX) Please choose 1-9. > "))
        refresh_screen()
    # check if cell is empty
    while board.cells[x_choice] != " ":
        print("\nSorry, that cell is taken.\n")
        x_choice = int(input("\nX) Please choose 1-9. > "))
        refresh_screen()
    # update board on valid input
    board.update_cell(x_choice, "X")

    # check for X win
    if board.is_winner("X"):
        # if player X wins, break loop
        print(f"\nX wins!\n")
        play_again = input("Play again? (Y/N) > ").upper()
        if play_again == "Y":
            board.reset()
            continue
        else:
            break
    # check for tie
    if board.is_tie():
        # if it is a tie, tell the player and ask if they want to play again
        print(f"\nTie!\n")
        play_again = input("Play again? (Y/N) > ").upper()
        if play_again == "Y":
            board.reset()
            continue
        else:
            break

    # 0 turn
    refresh_screen()
    # get O input and update board
    o_choice = int(input("\nO) Please choose 1-9. > "))
    # check if input is valid
    # check if input is a number between 1-9
    while o_choice not in range(1, 10):
        print("\nSorry, that is not a valid choice.\n")
        o_choice = int(input("\nO) Please choose 1-9. > "))
        refresh_screen()
    # check if cell is empty
    while board.cells[o_choice] != " ":
        print("\nSorry, that cell is taken.\n")
        o_choice = int(input("\nO) Please choose 1-9. > "))
        refresh_screen()
    # update board on valid input
    board.update_cell(o_choice, "O")

    # check for O win
    if board.is_winner("O"):
        # if player O wins, break loop
        print(f"\nO wins!\n")
        play_again = input("Play again? (Y/N) > ").upper()
        if play_again == "Y":
            board.reset()
            continue
        else:
            break
    # check for tie
    elif board.is_tie():
        # if it is a tie, tell the player and ask if they want to play again
        print(f"\nTie!\n")
        play_again = input("Play again? (Y/N) > ").upper()
        if play_again == "Y":
            board.reset()
            continue
        else:
            break

# BUG LIST
# 1. if player inputs a letter, it crashes
# 2. does not pickup winner until next turn
# many issues here
