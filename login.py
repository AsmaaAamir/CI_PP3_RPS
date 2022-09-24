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

WORKSHEET = SHEET.worksheet("login")

# to access the usrname from sheet



def login_menu():
    """
    Gives the user the option to login or register.
    """
    print(" ")
    print("Have you been here before?\n")
    login_choice = input("""
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
    print(" ")
    print("-------------------  Sign Up  -----------------------")
    print(" ")
    print(" Lets get you registered....")
    print(" ")
    print("           Rules for registration ")
    print(" ")
    print(" + Username - Maximum of 10 characters.")
    print(" + Password - Between 6 - 10 characters, it can have \n  number and sysmbols.")
    print(" ")
    print("------------------------------------------------------")
    print(" ")
    print("------------------- Your Details ----------------------")
    print(" ")

    user = WORKSHEET.col_values(1)
    pword = WORKSHEET.col_values(2)
    eaddress = WORKSHEET.col_values(3)

    username = user.append_input("Create a username: \t")
    password = pword.append_input("Enter your password: \t")
    password1 = input("Confirm the password: \t")
    email = eaddress.append_input("Enter your email address: \t")


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
