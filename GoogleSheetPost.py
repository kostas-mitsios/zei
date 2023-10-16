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
