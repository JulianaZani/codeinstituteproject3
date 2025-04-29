# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import gspread
from google.oauth2.service_account import Credentials

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPES)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('project03')

def get_votes_data():
    """
    Get votes figures input from the user.
    """
    print("Please enter votes data from the last search.")
    print("Data should be 5 numbers, separated by commas.")
    print("Assumption: 50,100,120,140,200,\n")

    data_str = input("Enter your data here: ")
    votes_data = data_str.split(",")
    validate_data(votes_data)

def validate_data(values):
    """
    Converts string values ​​to integers.
    Raises ValueError if strings cannot be converted into int,
    or if there aren't exactly 5 values.
    """
    try:
        if len(values) != 5:
            raise ValueError(
                f"Exactly 5 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
    
get_votes_data()