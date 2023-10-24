# tic tac toe game using classes
import os
from re import T

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
    refresh_screen()

    # get X input
    x_choice = int(input("\nX) Please choose 1-9. > "))

    # update board
    board.update_cell(x_choice, "X")

    o_choice = int(input("\nO) Please choose 1-9. > "))

    board.update_cell(o_choice, "O")
