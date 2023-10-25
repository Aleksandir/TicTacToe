# tic tac toe game using classes
from curses.ascii import isdigit
import os
from random import randint

os.system("clear")


class Board:
    """Represents a Tic Tac Toe board.

    Attributes:
        cells (list): A list of 10 strings representing the cells of the board.
            The first element is ignored, so the cells are numbered from 1 to 9.
            An empty cell is represented by a space character.
        corners (list): A list of 4 integers representing the indices of the corner cells.
        edges (list): A list of 4 integers representing the indices of the edge cells.
        win_conditions (tuple): A tuple of 8 tuples representing the winning conditions
            in the game. Each inner tuple contains the indices of the cells that need
            to be filled with the same mark in order to win the game.

    Methods:
        display(): Displays the current state of the board.
        update_cell(cell_num, player): Updates the specified cell with the player's mark.
        is_winner(player): Checks if the specified player has won the game.
        is_tie(): Checks if the game is a tie.
        reset(): Resets the board to its initial state.
        AI(player): Implements a simple AI to play the game.
    """

    def __init__(self):
        """Initializes a new instance of the Board class."""
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.corners = [1, 3, 7, 9]
        self.edges = [2, 4, 6, 8]
        self.win_conditions = (
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
            [1, 4, 7],
            [2, 5, 8],
            [3, 6, 9],
            [1, 5, 9],
            [3, 5, 7],
        )

    def display(self):
        """Displays the current state of the board."""
        print(f" {self.cells[1]} | {self.cells[2]} | {self.cells[3]} ")
        print("-----------")
        print(f" {self.cells[4]} | {self.cells[5]} | {self.cells[6]} ")
        print("-----------")
        print(f" {self.cells[7]} | {self.cells[8]} | {self.cells[9]} ")

    def update_cell(self, cell_num, player: str):
        """Updates the specified cell with the player's mark.

        Args:
            cell_num (int): The index of the cell to update (1-9).
            player (str): The mark to place in the cell ("X" or "O").
        """
        self.cells[int(cell_num)] = player

    def is_winner(self, player: str) -> bool:
        """Checks if the specified player has won the game.

        Args:
            player (str): The mark to check for ("X" or "O").

        Returns:
            bool: True if the player has won, False otherwise.
        """
        for condition in self.win_conditions:
            if (
                self.cells[condition[0]] == player
                and self.cells[condition[1]] == player
                and self.cells[condition[2]] == player
            ):
                return True
        return False

    def is_tie(self) -> bool:
        """Checks if the game is a tie.

        Returns:
            bool: True if the game is a tie, False otherwise.
        """
        if all(cell != " " for cell in self.cells[1:9]):
            return True
        else:
            return False

    def reset(self):
        """Resets the board to its initial state."""
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

    def AI(self, player: str):
        """Implements a simple AI to play the game.

        Args:
            player (str): The mark to use for the AI ("X" or "O").
        """
        if player == "X":
            enemy = "O"
        else:
            enemy = "X"

        # AI Behaviour:
        # 1. if die roll is 1, choose random cell
        # 2 if center is empty, choose center
        # 3. if enemy has 2 in a row, block
        # 4. if AI has 2 in a row, win
        # 5. if corner is empty, choose corner
        # 6. else choose random edge
        ai_mistake_chance = randint(1, 5)
        if ai_mistake_chance == 1:
            self.update_cell(randint(1, 9), player)
        elif self.cells[5] == " ":
            self.update_cell(5, player)
        else:
            for i, j, k in self.win_conditions:
                if self.cells[i] == self.cells[j] == enemy and self.cells[k] == " ":
                    self.update_cell(k, player)
                    return
                elif self.cells[i] == self.cells[k] == enemy and self.cells[j] == " ":
                    self.update_cell(j, player)
                    return
                elif self.cells[j] == self.cells[k] == enemy and self.cells[i] == " ":
                    self.update_cell(i, player)
                    return

            if any(self.cells[i] == " " for i in self.corners):
                for i in self.corners:
                    if self.cells[i] == " ":
                        self.update_cell(i, player)
                        return
            else:
                for i in self.edges:
                    if self.cells[i] == " ":
                        self.update_cell(i, player)
                        return


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


def player_move(player: str):
    refresh_screen()

    # get X input and update board
    choice = input(f"\n{player}) Please choose 1-9. > ")
    # check if input is valid
    # check if input is a number between 1-9
    while isdigit(choice) == False or int(choice) not in range(1, 10):
        print("\nSorry, that is not a valid choice.\n")
        choice = input(f"\n{player}) Please choose 1-9. > ")
        refresh_screen()
    # check if cell is empty
    while board.cells[int(choice)] != " ":
        print("\nSorry, that cell is taken.\n")
        choice = int(input(f"\n{player}) Please choose 1-9. > "))
        refresh_screen()
    # update board on valid input
    board.update_cell(choice, str(player))
    refresh_screen()


while True:
    # x turn
    player_move("X")

    # check for X win
    if board.is_winner("X"):
        # if player X wins, break loop
        print(f"\nX wins!\n")
        play_again = input("Play again? (Y/N) > ").upper()
        if play_again == "Y":
            board.reset()
            continue
        else:
            print("Game ended")
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
            print("Game ended")
            break

    # 0 turn
    # player_move("O")
    board.AI("O")
    refresh_screen()

    # check for X win
    if board.is_winner("O"):
        # if player X wins, break loop
        print(f"\nO wins!\n")
        play_again = input("Play again? (Y/N) > ").upper()
        if play_again == "Y":
            board.reset()
            continue
        else:
            print("Game ended")
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
            print("Game ended")
            break
