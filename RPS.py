"""Rock-Paper-Scissors game designed by Calvin Liu"""
import Tkinter
import ttk
import sys
import random
import time

class RockPaperScissors(object):
    """Base class for defining all the functions used in rock paper scissors"""

    # Used to keep track of which hand the player and the opponent has
    # Also used to compare hands and see who won the round
    player_rock = False
    player_paper = False
    player_scissors = False
    opp_rock = False
    opp_paper = False
    opp_scissors = False

    # If try_again is true, the round counter will continue to increment
    # if try_again is false, the round counter will NOT increment
    try_again = False

    # Summary is the variable that displays the winner of the round
    summary = ""

    # Counters to keep track of the win/lose record of the players
    player_wins = 0
    opp_wins = 0
    round_counter = 0

    def button_press(self, value):
        """Calls a series of functions when a button is pressed"""

        self.reset_hands()

        self.increment_round(self.try_again)

        self.player_hand(value)

        self.opponent_hand()

        self.compare_hands()

    def increment_round(self, try_again):
        """Keeps track of how many rounds have been played and how many wins each player has"""

        if try_again is False:

            # Increments the counter
            self.round_counter += 1
            round_value = "PLAYER: {}".format(self.player_wins) + (" " * 62) + "ROUND {}".format(
                self.round_counter) + (" " * 62) +"OPPONENT: {}".format(self.opp_wins)

            # Clear the round entry box
            self.round_entry.delete(0, "end")

            # Insert the new value to display the win/lose record
            self.round_entry.insert(0, round_value)

    def player_hand(self, value):
        """Determines what state the player's hand is in: rock, paper, or scissors"""

        # r = rock, p = paper, s = scissors
        if value == 'r':

            player_hand_value = (" " * 72) + "PLAYER:   ROCK"
            self.player_rock = True
            print("Player chose Rock.")

        elif value == 'p':

            player_hand_value = (" " * 72) + "PLAYER:   PAPER"
            self.player_paper = True
            print("Player chose Paper.")

        elif value == 's':

            player_hand_value = (" " * 72) + "PLAYER:   SCISSORS"
            self.player_scissors = True
            print("Player chose Scissors.")

        # Clear the player hand entry box
        self.player_hand_entry.delete(0, "end")

        # Insert the new value of what the player has chosen as their hand
        self.player_hand_entry.insert(0, player_hand_value)

    def opponent_hand(self):
        """Randomly generates a hand for the opponent using randint() function"""

        # 1 = rock, 2 = paper, 3 = scissors
        random_hand = random.randint(1, 3)

        # Slows down the pace of the game with pauses
        self.loading(0.5)

        if random_hand == 1:

            opp_hand_value = (" " * 72) + "OPPONENT:   ROCK"
            self.opp_rock = True
            print("Opponent chose Rock.")

        elif random_hand == 2:

            opp_hand_value = (" " * 72) + "OPPONENT:   PAPER"
            self.opp_paper = True
            print("Opponent chose Paper.")

        elif random_hand == 3:

            opp_hand_value = (" " * 72) + "OPPONENT:   SCISSORS"
            self.opp_scissors = True
            print("Opponent chose Scissors.")

        # Clear the opponent hand entry box
        self.opp_hand_entry.delete(0, "end")

        # Insert the value of the randomized hand of the opponent
        self.opp_hand_entry.insert(0, opp_hand_value)

    def compare_hands(self):
        """compares the hand of the player and the opponent to determine
        who the winner of the round is."""

        # Slows down the pace of the game with pauses
        self.loading(0.25)

        # If the round ends in a tie, the try_again will be set to true so that the program knows
        # to restart the round without incrementing the round number or changing the win/lose record
        if (self.player_rock is True and self.opp_rock is True) or (
                self.player_paper is True and self.opp_paper is True) or (
                    self.player_scissors is True and self.opp_scissors is True):

            self.try_again = True

            self.player_tie()

        else:

            # If there is no draw, then the code proceeds to determine the winner and the loser.
            self.try_again = False

            if self.player_rock is True and self.opp_scissors is True:

                self.player_win()

            elif self.player_rock is True and self.opp_paper is True:

                self.player_lose()

            elif self.player_paper is True and self.opp_rock is True:

                self.player_win()

            elif self.player_paper is True and self.opp_scissors is True:

                self.player_lose()

            elif self.player_scissors is True and self.opp_paper is True:

                self.player_win()

            elif self.player_scissors is True and self. opp_rock is True:

                self.player_lose()

        # Clear the summary entry box
        self.summary_entry.delete(0, "end")

        # Insert a new value which lets the player know if they won that round
        self.summary_entry.insert(0, self.summary)

    def reset_hands(self):
        """Ran after every match to reset the hand of the player and the opponent."""

        self.player_rock = False
        self.player_paper = False
        self.player_scissors = False
        self.opp_rock = False
        self.opp_paper = False
        self.opp_scissors = False

    def player_win(self):
        """Function that displays on screen that the player has won."""

        self.summary = (" " * 83) + "YOU WIN"
        print("Player wins against opponent.\n")
        self.player_wins += 1

    def player_lose(self):
        """Function that displays on screen that the opponent has won."""

        self.summary = (" " * 83) + "YOU LOSE"
        print("Player loses against opponent.\n")
        self.opp_wins += 1

    def player_tie(self):
        """Function that displays on screen that the round ended in a draw."""

        self.summary = (" "* 78) + "TIE. TRY AGAIN"
        print("Match ends in a draw.\n")

    @staticmethod
    def loading(delay):
        """Function that simulates the game loading."""

        for i in range(3):

            print ".",
            sys.stdout.flush()
            time.sleep(delay)

        print("")

    def __init__(self, root):

        # These variables will display the following strings when the game is ran
        self.round_val = Tkinter.StringVar(
            root, value="Welcome to the Rock-Paper-Scissors App developed by Calvin Liu")

        self.opp_hand_val = Tkinter.StringVar(
            root, value="Your opponent is waiting for you to start the game."
            " Game will record your win/lose record.")

        self.player_hand_val = Tkinter.StringVar(
            root, value="You can tart playing by picking a hand."
            " You can choose Rock, Paper, or Scissors.")

        self.summary_val = Tkinter.StringVar(
            root, value="The rules are: Rock beats Scissors."
            "Scissors beat Paper. Paper beats Rock.")

        # Define title for the app
        root.title("Rock-Paper-Scissors")

        # Defines the width and height of the window (can vary for different computers)
        root.geometry("579x216")

        # Stops resizing of the window
        root.resizable(width=False, height=False)

        # Customize the styling for the buttons and entry
        style = ttk.Style()

        style.configure("TButton", font="Serif 20", padding=10)
        style.configure("TEntry", font="Serif 25", padding=10)

        # This displays the number of rounds played and the win/lose record
        self.round_entry = ttk.Entry(root, textvariable=self.round_val, width=92)
        self.round_entry.grid(row=0, columnspan=3)

        # This displays the hand that the opponent has

        self.opp_hand_entry = ttk.Entry(root, textvariable=self.opp_hand_val, width=92)
        self.opp_hand_entry.grid(row=1, columnspan=3)

        # This displays the hand that the player has

        self.player_hand_entry = ttk.Entry(root, textvariable=self.player_hand_val, width=92)
        self.player_hand_entry.grid(row=2, columnspan=3)

        # This displays the winner of the round

        self.summary_entry = ttk.Entry(root, textvariable=self.summary_val, width=92)
        self.summary_entry.grid(row=3, columnspan=3)

        # Contains three buttons: Rock, Paper, and Scissors
        self.rock_button = ttk.Button(root, text="Rock", command=lambda: self.button_press('r'))
        self.rock_button.grid(row=4, column=0)

        self.paper_button = ttk.Button(root, text="Paper", command=lambda: self.button_press('p'))
        self.paper_button.grid(row=4, column=1)

        self.scissor_button = ttk.Button(
            root, text="Scissors", command=lambda: self.button_press('s'))
        self.scissor_button.grid(row=4, column=2)


# Increase compatability with Linux
if __name__ == '__main__':

    #Get the root window object
    root = Tkinter.Tk()

    # Create the game
    RPS = RockPaperScissors(root)

    # Run the app until exited
    root.mainloop()
