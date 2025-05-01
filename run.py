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

# -------------- Data Entry Functions ---------------------------

def get_votes_data(prompt_title):
    """
    Get votes data input from the user and validate it.
    """
    while True:
        print(prompt_title)
        print("Data should be 5 numbers, separated by commas.")
        print("Assumption: 50,100,120,140,200,\n")

        data_str = input("Enter your data here: ")
        votes_data = data_str.split(",")
        
        # Validate input; repeat prompt if invalid
        if validate_data(votes_data):
            print("Data is valid!\n")
            break

    # Convert input strings to integers before returning
    int_data = [int(value.strip()) for value in votes_data]
    return int_data

def validate_data(values):
    """
    Converts string values ​​to integers.
    Raises ValueError if there aren't exactly 5 values
    or if any value cannot be converted to an integer.
    """
    try:
        # Check if there are exactly 5 values
        if len(values) != 5:
            raise ValueError(
                f"Exactly 5 values required, you provided {len(values)}"
            )
        
        # Try converting each value to an integer
        [int(value.strip()) for value in values]
   
    except ValueError as e:
        # Print error message and return False if validation fails
        print(f"Invalid data: {e}, please try again.\n")
        return False
    return True

def update_worksheet(data, worksheet_name):
    """
    Update a specific worksheet with the provided data.
    """
    print(f"Updating '{worksheet_name}' worksheet...\n")
    worksheet = SHEET.worksheet(worksheet_name)
    worksheet.append_row(data)
    print(f"'{worksheet_name}' worksheet successfully updated.\n")

# -------------- Analysis Functions ---------------------------

def get_all_data(worksheet_name):
    """
    Retrieve all data from a specified worksheet.
    """
    worksheet = SHEET.worksheet(worksheet_name)
    data = worksheet.get_all_values()
    headers = data[0]
    rows = data[1:]
    return headers, [[int(value) for value in row] for row in rows]

def calculate_column_averages(data):
    """
    Calculate the average of each column in a specified worksheet.
    """
    transposed = list(zip(*data))
    return [round(sum(col) / len(col), 2) for col in transposed]

def update_averages_sheet(headers, averages, worksheet_name='Averages'):
    """
    Update the averages worksheet with the calculated averages.
    """
    worksheet = SHEET.worksheet(worksheet_name)
    worksheet.clear()
    worksheet.append_row(headers)
    worksheet.append_row(averages)

# ------------------- Main Function ---------------------------

def main():
    """
    Main program execution.
    """
    print("Welcome to the voting data input program!\n")
    print("This program collects data for both preferred and rejected candidates.\n")

    # Get votes for preferred candidates
    votes_data = get_votes_data("Question 1: Who would you vote for as mayor of Code City?")
    update_worksheet(votes_data, "Votes")

    # Get votes for candidates the user would never vote for
    print("\nNow let's enter the data for the candidates you would never vote for:\n")
    not_votes_data = get_votes_data("Question 2: Who would you never vote for as mayor of Code City?")
    update_worksheet(not_votes_data, "DoNotVote")

    # Automatic analysis
    vote_headers, vote_data = get_all_data("Votes")
    _, reject_data = get_all_data("DoNotVote")

    avg_votes = calculate_column_averages(vote_data)
    avg_rejects = calculate_column_averages(reject_data)

    update_averages_sheet(vote_headers, avg_votes)

    print("Thank you! Both sets of data have been saved.\n")
    print("Analytics and summary completed.\n")

main()