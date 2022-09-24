import gspread
from google.oauth2.service_account import Credentials

# Scope from Code Istituet Love Sandwiches walk-through project

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
    pass


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
