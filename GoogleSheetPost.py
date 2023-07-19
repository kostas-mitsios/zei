import os
import gspread
from google.oauth2 import service_account

# Replace 'path/to/your/credentials.json' with the actual path to your credentials file.
credentials = service_account.Credentials.from_service_account_file('path/to/your/credentials.json')
client = gspread.authorize(credentials)

# Replace '1sm_ePXHiTxty5gHfgW_rWGhzdnml1G6sVfuwKfKWeMM' with your actual Google Sheet ID.
sheet_id = '1sm_ePXHiTxty5gHfgW_rWGhzdnml1G6sVfuwKfKWeMM'
# Replace 'Dogs' with the name of the specific sheet you want to post data to.
sheet_name = 'Dogs'
sheet = client.open_by_key(sheet_id).worksheet(sheet_name)

# Replace data_list with the list of data you want to post to the sheet.
# Each element in data_list represents a row of data in the sheet.
data_list = [
    ['Buddy', 5, 'Labrador'],
    ['Max', 3, 'Golden Retriever'],
    ['Lucy', 2, 'Poodle'],
]

# Update the data in the specific range (A14:C16).
# This assumes that your data_list has exactly three rows (3 elements).
sheet.update('A14:C16', data_list)
