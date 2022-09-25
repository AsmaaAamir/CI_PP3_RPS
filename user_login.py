import gspread
from google.oauth2.service_account import Credentials

import re

# from run import home_screen, game

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


def login_menu():
    """
    Gives the user the option to login or register.
    """
    print(" ")
    print("Have you been here before?\n")
    login_choice = input("""
        1. Yes
        2. No
        3. Home Page\n
        Please enter your option: \t""")
    if login_choice == "1":
        existing_players(login)
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
    """
    print(" ")
    print("-------------------  Sign Up  -----------------------")
    print(" ")
    print(" Lets get you registered....")
    print(" ")
    print("           Rules for registration ")
    print(" ")
    print(" + Username - Maximum of 10 characters.")
    print(" + Password - Between 6 - 10 characters, it can have \n  number and 1 capital letter")
    print(" ")
    print("------------------- Your Details ----------------------")
    print(" ")
    username = input("Create a username: \t")
    password = input("Enter your password: \t")
    email = input("Enter your email address: \t")
    user_details = [username, password, email]
    login.append_row(user_details)
    update_login_worksheet()


def validate_register_user(username):
    """
    Raises any errors in Username and passwords if they meet the rules,
    stated in the register varibale.
    """
    while True:
        if len(username) > 10:
            print("Make sure your username is maximum of 10 characters")
        else:
            print("Saving your Username ")
            break


def validate_register_password(password):
    """
    Raises any errors in Username and passwords if they meet the rules,
    stated in the register varibale.
    """
    while True:
        if len(password) < 6:
            print("Make sure your password is atleast 6 characters")
        elif re.search('[0-9]', password) is None:
            print("Make sure your password has a number in it")
        elif re.search('[A-Z]', password) is None:
            print("Make sure your password has a capital letter in it")
        else:
            print("Saving you password")
            break


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


def existing_players(login):
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
    username = input("Username: \t")
    password = input("Password: \t")
    for row in login:
        if row[0] == username:
            print("Player found, please enter your password")
            break
        elif row[0] == password:
            print("Welcome Back")
        else:
            print("Player not found!!")
            existing_players(login)


login_menu()
register()
validate_register_user(username)
validate_register_password(password)
update_login_worksheet()
existing_players(login)



