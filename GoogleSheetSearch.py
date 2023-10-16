import gspread
from oauth2client.service_account import ServiceAccountCredentials
import requests

#credentials
credentials_file = 'C:/Users/kmitsios/Downloads/credentials.json'
api_key = 'AIzaSyDowT_pE8qSIUtJrTa7AsBWj6X2wR8migw'

#create session
session = requests.Session()
session.headers.update({'Authorization': f'Bearer {api_key}'})

# Authenticate with Google Sheets API using the custom session
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(credentials_file, scope)
client = gspread.Client(auth=credentials, session=session)

# Open the Google Sheet by its ID
sheet_id = "1sm_ePXHiTxty5gHfgW_rWGhzdnml1G6sVfuwKfKWeMM"
sheet = client.open_by_key(sheet_id)

# Specify the named range
named_range = "dogs"

# Get all values from the named range
range_data = sheet.values_get(named_range)

if "values" in range_data:
    # Search for the value "aaa" in column A and retrieve all other data from the same row
    search_value = "aaa"
    for row_values in range_data["values"]:
        if row_values[0] == search_value:  # Check if the value is found in column A
            print("Data from the row containing 'aaa':", row_values)
            break  # Stop searching after the first match
else:
    print("Named range 'dogs' not found.")