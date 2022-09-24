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
    pass


def register():
    pass


def validate_register():
    pass


def update_login_worksheet():
    pass


def existing_players():
    pass


login_menu()
register()
validate_register()
update_login_worksheet()
existing_players()

