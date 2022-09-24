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
SHEET = GSPREAD_CLIENT.open('login_details').sheet1


def login_menu():
    """
    Gives the user the option to login or register.
    """
    print(" ")
    print("Have you been here before>\n")
    login_choice = input(""""
        1. Yes
        2. No \n
        Please enter your option: \t""")
    if login_choice == "1":
        existing_players()
    elif login_choice == "2":
        register()
    else:
        print("Please select one of the above options: \t \n")
        return


def register():
    """
    Allows user to enter their details for registeration.
    """
    pass


def validate_register():
    """
    Raises any errors in Username and passwords if they meet the rules,
    stated in the register varibale.
    """
    pass


def update_login_worksheet():
    """
    Update the login sheet with new players details, their username, password
    and email addess.
    """
    pass


def existing_players():
    """
    Allowing returing player to login to play the game.
    Player will need to use there username and password to login.
    The usernae is retrieved from the first column in login sheet.
    The password is retrieved from the second column from login details.
    """
    pass


login_menu()
register()
validate_register()
update_login_worksheet()
existing_players()
