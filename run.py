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
    Get votes data input from the user and validate it.
    """
    while True:
        print("Please enter votes data from the last search.")
        print("Data should be 5 numbers, separated by commas.")
        print("Assumption: 50,100,120,140,200,\n")

        data_str = input("Enter your data here: ")
        votes_data = data_str.split(",")
        
        if validate_data(votes_data):
            print("Data is valid!\n")
            break

    int_data = [int(value.strip()) for value in votes_data]
    return int_data

def validate_data(values):
    """
    Converts string values ​​to integers.
    Raises ValueError if there aren't exactly 5 values
    or if any value cannot be converted to an integer.
    """
    try:
        if len(values) != 5:
            raise ValueError(
                f"Exactly 5 values required, you provided {len(values)}"
            )
        [int(value.strip()) for value in values]
   
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False
    return True

def update_votes_worksheet(data):
    """
    Update voting spreadsheet, add new row with new survey data.
    """
    print("Updating vote spreadsheet...\n")
    votes_worksheet = SHEET.worksheet("Votes")
    votes_worksheet.append_row(data)
    print("Spreadsheet with votes successfully updated.\n")


def main():
    """
    Main function to run the program.
    """
    print("Welcome to the voting data input program!\n")
    print("This program will help you input your votes data into a spreadsheet.\n")
    
    # Get votes data from user
    data = get_votes_data()
    
    # Update the votes worksheet with the new data
    update_votes_worksheet(data)