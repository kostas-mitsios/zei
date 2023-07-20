import tkinter as tk
import pandas as pd
import win32com.client as win32com
import requests
import json
import getpass
from tkinter.ttk import *
import psutil as psu
import time

#Get username and default path based on username
username = getpass.getuser()
mitsiosPath = " (1)"
if username == 'kmitsios':
    accServicePath = fr'C:\Users\{username}\International Organization for Migration - IOM\HELIOS - Documents{mitsiosPath}\Information Management\Projects\Accommodations Tools\Accommodation Service CSV tool'
elif username == 'gpolitis':
    accServicePath = fr'C:\Users\{username}\International Organization for Migration - IOM\HELIOS - Information Management\Projects\Accommodations Tools\Accommodation Service CSV tool'
else:
    accServicePath = fr'C:\Users\{username}\International Organization for Migration - IOM\HELIOS - Documents\Information Management\Projects\Accommodations Tools\Accommodation Service CSV tool'
if username == "kmitsios":
    matchMakingPath = fr'C:\Users\{username}\International Organization for Migration - IOM\HELIOS - Documents{mitsiosPath}\Information Management\Projects\Accommodations Tools\Match Making Tools CSV tool'
elif username == 'gpolitis':
    matchMakingPath = fr'C:\Users\{username}\International Organization for Migration - IOM\HELIOS - Information Management\Projects\Accommodations Tools\Match Making Tools CSV tool'
else:
    matchMakingPath = fr'C:\Users\{username}\International Organization for Migration - IOM\HELIOS - Documents\Information Management\Projects\Accommodations Tools\Match Making Tools CSV tool'
if username == "kmitsios":
    monthlyDisbursementsPath = fr'C:\Users\{username}\International Organization for Migration - IOM\HELIOS - Documents{mitsiosPath}\Information Management\Projects\Monthly Disbursements\KoBoCsv'
elif username == 'gpolitis':
    monthlyDisbursementsPath = fr'C:\Users\{username}\International Organization for Migration - IOM\HELIOS - Information Management\Projects\Monthly Disbursements\KoBoCsv'
else:
    monthlyDisbursementsPath = fr'C:\Users\{username}\International Organization for Migration - IOM\HELIOS - Documents\Information Management\Projects\Monthly Disbursements\KoBoCsv'

#Creating arrays in the same order, so that a simple loop can iterate through them and refresh/update the correct files on the correct forms
pathList = [accServicePath, matchMakingPath, monthlyDisbursementsPath]
fileList = ["accservice_csv", "mmaking_csv", "md_csv"]
xformIDList = [975448, 1219842, 1159370]

# Kill any Excel process running at the moment
def killExcel():
    for proc in psu.process_iter():
        if proc.name() == "EXCEL.EXE" or proc.name() == "excel.exe":
            proc.kill()
            time.sleep(2)

def refreshCSV(p, f, x):
    #Refresh all Queries in a single file
    #triesRemaining = 100 #unused atm, purpose is to try 100 times to open each file, in order to make sure that it works even in slower machines
    failsafe = False #invoked if an exception occurs and file processing will not consist after being refreshed+saved
    #while triesRemaining > 0: #loop for 100 openings. Add indent if used
    try:
        print(f"Refreshing {f}.csv")
        xlapp = win32com.DispatchEx("Excel.Application")
        xlapp.Visible = False
        wb = xlapp.Workbooks.Open(f"{p}\\{f}.xlsx")
        time.sleep(1) #sleep for 1" to have time to properly finish prior process
        wb.RefreshAll()
        xlapp.CalculateUntilAsyncQueriesDone()
        time.sleep(1) #sleep for 1" to have time to properly finish prior process
        wb.Save()
        time.sleep(10) #sleep for 1" to have time to properly finish prior process
        wb.Close()
        #time.sleep(1) #sleep for 3" to have time to properly finish prior process
        xlapp.Quit()
        #time.sleep(1) #sleep for 3" to have time to properly finish prior process
        del wb
        #time.sleep(1) #sleep for 3" to have time to properly finish prior process
        del xlapp
        print(f"{f}.csv was successfully refreshed")

        #use pandas to open excel file and save as CSV UTF-8 encoding
        read_file = pd.read_excel(f"{p}\\{f}.xlsx")
        read_file.to_csv(f"{p}\\{f}.csv", index = None, header = True, encoding="utf_8_sig")
        print(f"{f}.csv was successfully saved")
    except:
        #traceback.print_exc()
        #triesRemaining -= 1 #loop escape
        if wb is not None:
            del wb
        del xlapp
        killExcel() #kill all running excel instances
        failsafe = True
        print(f"{f}.csv was NOT refreshed and was skipped")


    if failsafe == False:
        #post media file to KoBo form
        KC_URL = 'https://kc.humanitarianresponse.info/api/v1'
        TOKEN = '51e64ca25a8ee39573bbeedaaeef65203ea49d99'
        XFORM = x
        HEADERS = {'Authorization': f'Token {TOKEN}'}

        FILE_FOLDER = p
        FILENAME = f'{f}.csv'
        MIME = 'text/csv'

        files = {'data_file': (FILENAME, open(
            fr'{FILE_FOLDER}/{FILENAME}', 'rb').read(), MIME)}
        data = {
            'data_value': FILENAME,
            'xform': XFORM,
            'data_type': 'media',
            'data_file_type': MIME,
        }

        # Download metadata.json
        response = requests.get(fr"{KC_URL}/metadata.json", headers=HEADERS, verify=False)
        dict_response = json.loads(response.text)

        # Delete appropriate entry in the metadata.json (delete old file)
        for each in dict_response:
            if each['xform'] == XFORM and each['data_value'] == FILENAME:
                del_id = each['id']
                response = requests.delete(
                    fr"{KC_URL}/metadata/{del_id}", headers=HEADERS, verify=False)
                break
        print(f"Previous {f}.csv was successfully deleted")

        #alternative post with verify=false on SSL
        # Upload the changed file
        response = requests.post(
            fr"{KC_URL}/metadata.json", data=data, files=files, headers=HEADERS, verify=False)
        print(fr"{f} was successfully uploaded")
        return 1

        """
        # Upload the changed file
        response = requests.post(
            fr"{KC_URL}/metadata.json", data=data, files=files, headers=HEADERS)
        print(fr"{f} was successfully uploaded")
        return 1
        """
    return 0

def button_click(button_name):
    try:
        index = fileList.index(button_name)
        path = pathList[index]
        file = fileList[index]
        xformID = xformIDList[index]
        refreshCSV(path, file, xformID)
    except ValueError:
        print(f"Button '{button_name}' not found in the fileList.")

#refresh all CSVs
def refresh_all_csv():
    for name in button_names:
        button_click(name)

# Create the GUI
root = tk.Tk()
root.title("Refresh CSVs")

# Create buttons for each file
button_names = ["accservice_csv", "mmaking_csv", "md_csv"]

for name in button_names:
    button = tk.Button(root, text=name, command=lambda name=name: button_click(name))
    button.pack(pady=5)

# Create the "Refresh all CSV" button
refresh_all_button = tk.Button(root, text="Refresh all CSV", command=refresh_all_csv)
refresh_all_button.pack(pady=10)

root.mainloop()