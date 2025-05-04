# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
# Description:
# This script collects voting and rejection data for candidates,
# stores the data in Google Sheets, calculates averages,
# identifies top/rejected candidates, and shows percentage charts.

import os
import platform
import gspread
from google.oauth2.service_account import Credentials

# -------------- Clear Screen Function -------------------------


def clear_console():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

# -------------- Google Sheets Setup ---------------------------


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
        print("Example: 50,100,120,140,200\n")

        data_str = input("Enter your data here: ").strip()

        if not data_str:
            print(
                "No input provided." 
                "Please enter 5 numbers separated by commas.\n"
            )
            continue

        votes_data = data_str.split(",")

        if validate_data(votes_data):
            print("Data is valid!\n")
            break

    int_data = [int(value.strip()) for value in votes_data]
    return int_data


def validate_data(values):
    """
    Validates the user input data:
    - Ensures input is not empty
    - Checks if exactly 5 values were provided
    - Checks if all values can be converted to integers
    """
    if len(values) != 5:
        print(
            f"Invalid data: Exactly 5 values are required," 
            f"you provided {len(values)} data.\n"
        )
        return False

    try:
        [int(value.strip()) for value in values]
    except ValueError:
        print(
            "Invalid data: All inputs must be numbers."
            "Please try again.\n"
        )
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
    input("\nPress Enter to continue...")
    print("Please wait while we process the data...\n")

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


def generate_summary(headers, avg_votes, avg_rejects):
    """
    Generate a summary with top voted and most rejected candidates.
    """
    most_voted_index = avg_votes.index(max(avg_votes))
    most_rejected_index = avg_rejects.index(max(avg_rejects))

    summary_data = [["Top Voted Candidate",
                     headers[most_voted_index],
                     avg_votes[most_voted_index]],
                    ["Most Rejected Candidate",
                     headers[most_rejected_index],
                     avg_rejects[most_rejected_index]],
                    ]

    return summary_data


def update_summary_sheet(summary_data, worksheet_name='Summary'):
    """
    Update the summary worksheet with the generated summary data.
    """
    worksheet = SHEET.worksheet(worksheet_name)
    worksheet.clear()
    worksheet.append_row(["Description", "Candidate", "Average"])

    for row in summary_data:
        worksheet.append_row(row)


def display_percentages(headers, averages, title):
    """
    Display the averages as percentages in the terminal.
    """
    total = sum(averages)
    print(f"\n{title}")
    print("-" * len(title))
    for name, avg in zip(headers, averages):
        percentage = (avg / total) * 100 if total else 0
        print(f"{name}: {percentage:.2f}%")

# ------------------- Main Function ---------------------------


def main():
    """
    Main program execution with option to repeat.
    """
    clear_console()
    print("Welcome to the voting data input program!\n")
    print(
        "This program collects data for both"
        "preferred and rejected candidates.\n"
    )

    while True:
        votes_data = get_votes_data(
            "How many votes did each candidate"
            " for mayor of Code City get?"
        )
        update_worksheet(votes_data, "Votes")

        clear_console()

        print(
            "Now let's enter the data for the candidates"
            "you would never vote for:\n"
        )
        not_votes_data = get_votes_data(
            "How many rejection votes did each candidate get?"
            )
        update_worksheet(not_votes_data, "DoNotVote")

        vote_headers, vote_data = get_all_data("Votes")
        _, reject_data = get_all_data("DoNotVote")

        avg_votes = calculate_column_averages(vote_data)
        avg_rejects = calculate_column_averages(reject_data)

        update_averages_sheet(vote_headers, avg_votes)

        summary = generate_summary(vote_headers, avg_votes, avg_rejects)
        update_summary_sheet(summary)

        print(
            "Thank you!" 
            "Both sets of data have been saved.\n"
        )

        print("Analytics and summary completed.\n")

        input("\nPress Enter to continue...")

        clear_console()

        display_percentages(
            vote_headers,
            avg_votes,
            "Average Votes (%) per Candidate")
        display_percentages(
            vote_headers,
            avg_rejects,
            "Average Rejections (%) per Candidate")

        repeat = input(
            "\nDo you want to enter more data? (yes/no): ").strip().lower()
        if repeat not in ["yes", "y"]:
            print(
                "Goodbye!" 
                "Thank you for using the voting data program."
            )
            break


main()
