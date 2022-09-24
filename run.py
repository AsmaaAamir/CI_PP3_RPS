import random


def home_screen():
    """
    Welcome page with heading and main menu.
    """
    print(" ")
    print("   Welcome  to ")
    print(" ")
    print("           Rock\n ")
    print("                Paper\n")
    print("                       Sissors\n")
    print(" ")
    print(" ")

    print("------------------  Main Menu  ------------------------")

    while True:
        home_choice = input("""
            1. Game Rules
            2. Play the Game\n
            Please enter your choice:\t """)

        if home_choice == "1":
            game_rules()
        elif home_choice == "2":
            game()
        else:
            print("You can only select either 1 or 2")
            print("Please enter your choice: \t")
            home_screen()


def game_rules():
    """
    Game rules - breifly explainging the user how to play the game.
    how to win the game and how the user can lose the game.
    I got the game rules from google.
    """
    print("------------------  Game Rules  -----------------------")
    print(" ")
    print("The rules are very simple:- ")
    print(" ")
    print("1. You would be playing againt the computer.")
    print("2. You can choose between Rock, Paper and Siccsors.")
    print("3. You type in your choose then it the computer display it choice.\n")
    print("Ways your can  *** WIN *** ")
    print(" ")
    print("1. If you choose Rock, you will win against Scissors,\n   but lose against Paper.")
    print("2. If you choose Paper, you will win against Rock,\n   but lose against Sissors.")
    print("3. If you choose Sicssors, you will win against Paper,\n   but lose against Rock.")
    print(" ")
    print("------------------------------------------------------")
    while True:
        gr_choice = input("""
            1. Play the Game
            2. Back to home page\n
            Please enter your choice:\t """)

        if gr_choice == "1":
            game()
        elif gr_choice == "2":
            home_screen()
        else:
            print("You can only select either 1 or 2")
            print("Please enter your choice: \t")
            game_rules()


def game():
    """
    Code for the game to play against the computer.
    """
    choices = ["rock", "paper", "sissors"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock, paper, or sissors? \t").lower()

        if player == computer:
            print("Computer: ", computer)
            print("Player: ", player)
            print("! Tie !")

        elif player == "rock":
            if computer == "sissors":
                print("Computer: ", computer)
                print("Player: ", player)
                print("** You Win **")
            if computer == "paper":
                print("Computer: ", computer)
                print("Player: ", player)
                print(":( You Lose ):")
        elif player == "paper":
            if computer == "rock":
                print("Computer: ", computer)
                print("Player: ", player)
                print("** You Win **")
            if computer == "sissors":
                print("Computer: ", computer)
                print("Player: ", player)
                print(":( You Lose ):")
        elif player == "sissors":
            if computer == "paper":
                print("Computer: ", computer)
                print("Player: ", player)
                print("** You Win **")
            if computer == "rock":
                print("Computer: ", computer)
                print("Player: ", player)
                print(":( You Lose ):")

    play_again = input("Play again? (Yes / No : "). lower()
    if play_again != "yes":
        g_choice = input("""
                    1. Play again
                    2. Back to home page\n
            Please enter your choice:\t """)

        if g_choice == "1":
            game()
        elif g_choice == "2":
            home_screen()
        else:
            print("You can only select either 1 or 2")
            print("Please enter your choice: \t")
            game_rules()


home_screen()
game_rules()
game()
