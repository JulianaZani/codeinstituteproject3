# Voting and Rejection Data Analyzer  

This terminal-based application allows users to input voting and rejection data for candidates, store the data in Google Sheets, and automatically analyze results with averages, top candidates, and summary percentages.  


## Description  

This script collects data regarding the most and least voted candidates.
The goal is to help analyze electoral preferences by calculating column averages, identifying the top-voted and most-rejected candidates, and displaying percentage charts.  

It integrates with Google Sheets using the gspread and google-auth libraries.  


## Features  

**Existing features**  
This project was developed to allow users to input, store, and analyze voting and rejection data for candidates directly through the terminal. When the program runs, the user is guided by clear instructions on how to properly enter the data. After validating the input, the script sends the data to specific worksheets on Google Sheets, separating positive votes and rejection votes into different tabs.

A key feature is the input validation system, which ensures that users provide exactly five numeric values separated by commas. If the input is invalid, informative error messages are displayed until the data is correctly formatted. Once the data is submitted, the program automatically retrieves all existing records from the spreadsheets, calculates the average votes and rejections for each candidate, and updates a worksheet with these averages.

Additionally, the script identifies the most voted and most rejected candidates and generates a short analytical summary, which is also sent to the spreadsheet. Finally, the terminal displays the results as percentages, making it easy to visually understand the distribution of votes and rejections per candidate.

The user interaction is clear and educational, making the process intuitive even for those with little technical experience.

**Future features**  

Among several possible implementations, in the future I intend to implement data visualization using graphs to help users better interpret the results. I will seek improvements to make the program more robust, easy to use and suitable for a wider range of real-world applications.


## How to Use  


## Data Model  


## Testing  

**Manual Testing**  

- All data inputs were validated to reject incorrect or incomplete formats.  
- Successfully tested reading and writing to Google Sheets.  
- Ensured calculations of averages and percentages return expected results.  
- Output was reviewed for clarity and usability in the terminal.  

**Validator Testing**  
- No errors were returned from PEP8 validator anymore.

**BEFORE**  
![pep8before](doc/screenshots/screenshotpep801.png)

**AFTER**  
![pep8after](doc/screenshots/screenshotpep802.png)


## Deployment  


## Credits  




![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **May 14, 2024**

## Reminders

- Your code must be placed in the `run.py` file
- Your dependencies must be placed in the `requirements.txt` file
- Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

---

Happy coding!
