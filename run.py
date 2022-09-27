import random
import gspread
from google.oauth2.service_account import Credentials


# scope and the constant vars are from love_sandwiches walkt-through project
# by code institute

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('login_details')

login = SHEET.worksheet("login")


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
            2. Login
            3. Exist \n
            Please enter your choice:\t\n """)

        if home_choice == "1":
            game_rules()
        elif home_choice == "2":
            login_menu()
        elif home_choice == "3":
            exit_game()
        else:
            print("You can only select either 1 to 3")
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
    print("3. You type in your choose then its the computer turn.")
    print(" ")
    print("------------------------------------------------------")
    print(" ")
    print("Ways your can  *** WIN *** ")
    print(" ")
    print("1.You choose Rock, you will win against Scissor\n   but lose against Paper.")
    print("2.You choose Paper, you will win against Rock\n  but lose against Sissor.")
    print("3.You choose Sicssor, you will win against Paper\n   but lose against Rock.")
    print(" ")
    print("------------------------------------------------------")
    while True:
        gr_choice = input("""
            1. Play the Game
            2. Login
            3. Back to home page\n
            Please enter your choice:\t \n""")

        if gr_choice == "1":
            game()
        elif gr_choice == "2":
            login_menu()
        elif gr_choice == "3":
            game()
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
    print(" ")
    print("------------------ Lets Start ------------------------")
    print(" ")
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
                break
            if computer == "paper":
                print("Computer: ", computer)
                print("Player: ", player)
                print(":( You Lose ):")
                break
        elif player == "paper":
            if computer == "rock":
                print("Computer: ", computer)
                print("Player: ", player)
                print("** You Win **")
                break
            if computer == "sissors":
                print("Computer: ", computer)
                print("Player: ", player)
                print(":( You Lose ):")
                break
        elif player == "sissors":
            if computer == "paper":
                print("Computer: ", computer)
                print("Player: ", player)
                print("** You Win **")
                break
            if computer == "rock":
                print("Computer: ", computer)
                print("Player: ", player)
                print(":( You Lose ):")
                break

    print("------------------  Play Again  ----------------------")
    print(" ")
    play_again = input("(Yes / No): \n").lower()
    print(" ")
    if play_again == "yes":
        game()
    elif play_again == "no":
        home_screen()


def login_menu():
    """
    Gives the user the option to login or register.
    """
    print(" ")
    print("------------------  Log In  ----------------------")
    print(" ")
    print("Have you been here before?\n")
    login_choice = input("""
        1. Yes
        2. No
        3. Home Page\n
        Please enter your option: \t""")
    if login_choice == "1":
        existing_players()
    elif login_choice == "2":
        register()
    elif login_choice == "3":
        home_screen()
    else:
        print("Please select one of the above options: \t \n")
        return


def register():
    """
    Allows user to enter their details for registeration.
    Raises any errors in Username and passwords if they meet the rules,
    stated in the register varibale.
    Raises any errors in Username and passwords if they meet the rules,
    stated in the register varibale.
    """
    print(" ")
    print("-------------------  Sign Up  -----------------------")
    print(" ")
    print(" Lets get you registered....")
    print(" ")
    print("           Rules for registration ")
    print(" ")
    print("+ Username - Maximum of 10 characters.")
    print("+ Password - Between 6 - 10 character numbers and 1 capital letter")
    print(" ")
    print("------------------- Your Details ----------------------")
    print(" ")
    username = input("Create a username: \t\n")
    password = input("Enter your password: \t\n")
    email = input("Enter your email address: \t\n")
    user_details = [username, password, email]
    login.append_row(user_details)
    update_login_worksheet()
    if len(username) >= 10:
        print("Username can't be more the 10 characters.")
        print("Choose another Username")
        register()
    elif username in login.findall(username):
        print("This username already exist. Please sign in")
        print("Re-try")
        register()
    else:
        register()
    if len(password) <= 6:
        print("Password can't be more the 10 characters.")
        print("Choose another password")
        register()
    else:
        update_login_worksheet()


def update_login_worksheet():
    """
    Update the login sheet with new players details, their username, password
    and email addess.
    """
    print(" ")
    print("--------------- Saving your details -----------------------")
    print(" ")
    print("------------------ Your registered ------------------------")
    while True:
        update_choice = input("""
            1. Play the Game
            2. Back to home page\n
            Please enter your choice:\t """)
        if update_choice == "1":
            game()
            break
        elif update_choice == "2":
            home_screen()
            break
        else:
            print("You can only select either 1 or 2")
            print("Please enter your choice: \t")
            login_menu()


def existing_players():
    """
    Allowing returing player to login to play the game.
    Player will need to use there username and password to login.
    The usernae is retrieved from the first column in login sheet.
    The password is retrieved from the second column from login details.
    """
    print(" ")
    print("----------------- Welcome Back ------------------------ ")
    print(" ")
    print(" Lets get you signed in ....")
    print(" ")
    username = input("Username: \t\n")
    password = input("Password: \t\n")
    if username != login.findall("Username"):
        print(" ")
        print("\n                Player found\n")
        print("                  Lets Play")
        print("\n-----------------------------------------------------\n")
        game()
    elif username == login.findall("Username"):
        print(" ")
        print("\n         No player found\n")
        print("    Please check details and try again\n")
    else:
        existing_players()
    if password != login.findall("Password"):
        game()
    elif password == login.findall("Password"):
        print("\n        No player found\n")
        print("    Please check details and try again\n")
    else:
        existing_players()


def exit_game():
    """
    Exit the programme when chosen from the main menu.
    """
    print("----------------- Thank you for playing --------------------")
    print("------------------ Have a lovely day! ------------------------")


home_screen()
game_rules()
game()
login_menu()
register()
update_login_worksheet()
existing_players()
exit_game()
