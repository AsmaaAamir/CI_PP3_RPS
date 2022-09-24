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
    """
    print("------------------  Game Rules  -----------------------")
    print(" ")
    print("The rules are very simple:- ")
    print(" ")
    print("1. Player would be playing againt the computer.")
    print("2. You can choose between Rock, Paper and Siccsors.")
    print("3. You type in your choose then it the computer display it choice.\n")
    print(" Ways your can *** WIN ***")


def game():
    """
    Code for the game to play against the computer.
    """
    pass   

home_screen()
game_rules()
game()
