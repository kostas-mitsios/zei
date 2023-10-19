"""
import os
import gspread
from google.oauth2 import service_account

# Replace 'path/to/your/credentials.json' with the actual path to your credentials file.
credentials = service_account.Credentials.from_service_account_file('C:/Users/katikako/Downloads/credentials.json')
client = gspread.authorize(credentials)

sheet_id = '1sm_ePXHiTxty5gHfgW_rWGhzdnml1G6sVfuwKfKWeMM'
sheet_name = 'Dogs'
sheet = client.open_by_key(sheet_id).worksheet(sheet_name)

# Each element in data_list represents is a row in the google sheet
data_list = [
    ['Buddy', 5, 'Labrador'],
    ['Max', 3, 'Golden Retriever'],
    ['Lucy', 2, 'Poodle'],
]

# Update the data in the specific range (A14:C16).
# Only 3 rows at the moment
sheet.update('A14:C16', data_list)

"""
import gspread
from google.oauth2 import service_account

# Define your credentials file path
credentials_file = 'credentials.json'

# Authenticate with Google Sheets API
scope = ["https://www.googleapis.com/auth/spreadsheets"]
credentials = service_account.Credentials.from_service_account_file(credentials_file, scopes=scope)
client = gspread.Client(auth=credentials)

# Open the Google Sheet by its ID
sheet_id = "1sm_ePXHiTxty5gHfgW_rWGhzdnml1G6sVfuwKfKWeMM"
sheet = client.open_by_key(sheet_id)

# Select the "Dogs" sheet by its title
worksheet = sheet.worksheet("Dogs")

# Define the data you want to write (e.g., as a list of lists)
data_to_write = [
    ["TestDog1", 2, "1/1/2023", "", "", "", "","Yes"],
    ["TestDog2", 0, "18/10/2023", "", "", "","", "No"]
]

# Find the first empty row in column A
next_empty_row = len(worksheet.col_values(1)) + 1

# Clear the existing data in the sheet (optional)
# worksheet.clear()

# Append the data to the sheet
worksheet.insert_rows(data_to_write, next_empty_row)  # You can specify the row number where data should be inserted

print("Data has been written to the 'Dogs' sheet.")
