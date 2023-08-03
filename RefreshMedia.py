import pandas as pd
from openpyxl import load_workbook
import win32com.client as win32com
#from tkinter import filedialog
#from tkinter import *
import requests
import json
import getpass
from tkinter import *
from tkinter.ttk import *
import psutil as psu
import time
#import traceback

"""select folder with the xlsx and csv files to be updated
#Open folder selection panel
root = Tk()
root.withdraw()
folder_to_Save = filedialog.askdirectory()
#print(folder_to_Save)
accServiceFile = 'accservice_csv'
mdFile = 'md_csv'
"""



#Get username and default path based on username
username = getpass.getuser()
if username == 'kmitsios':
    mitsiosPath = " (1)"
else:
    mitsiosPath = ""

path_internal_firstPart = fr'C:\Users\{username}\International Organization for Migration - IOM\HELIOS - Documents'
path_external_firstPart = ''


if username == 'gpolitis':
    accServicePath = fr'C:\Users\{username}\International Organization for Migration - IOM\HELIOS - Information Management\Projects\Accommodations Tools\Accommodation Service CSV tool'
else:
    accServicePath = fr'C:\Users\{username}\International Organization for Migration - IOM\HELIOS - Documents{mitsiosPath}\Information Management\Projects\Accommodations Tools\Accommodation Service CSV tool'
if username == 'gpolitis':
    matchMakingPath = fr'C:\Users\{username}\International Organization for Migration - IOM\HELIOS - Information Management\Projects\Accommodations Tools\Match Making Tools CSV tool'
else:
    matchMakingPath = fr'C:\Users\{username}\International Organization for Migration - IOM\HELIOS - Documents{mitsiosPath}\Information Management\Projects\Accommodations Tools\Match Making Tools CSV tool'
if username == 'gpolitis':
    monthlyDisbursementsPath = fr'C:\Users\{username}\International Organization for Migration - IOM\HELIOS - Information Management\Projects\Monthly Disbursements\KoBoCsv'
else:
    monthlyDisbursementsPath = fr'C:\Users\{username}\International Organization for Migration - IOM\HELIOS - Documents{mitsiosPath}\Information Management\Projects\Monthly Disbursements\KoBoCsv'
if username == 'gpolitis':
    individualsPath = fr'C:\Users\{username}\International Organization for Migration - IOM\HELIOS - Information Management\HELIOS Database\01 Individuals'
else:
    individualsPath = fr'C:\Users\{username}\International Organization for Migration - IOM\HELIOS - Documents{mitsiosPath}\Information Management\HELIOS Database\01 Individuals'
if username == 'gpolitis':
    outreachV2Path = fr'C:\Users\{username}\International Organization for Migration - IOM\HELIOS - Information Management\HELIOS Database\02 Outreach'
else:
    outreachV2Path = fr'C:\Users\{username}\International Organization for Migration - IOM\HELIOS - Documents{mitsiosPath}\Information Management\HELIOS Database\02 Outreach'
if username == 'gpolitis':
    heliosdbPath = fr'C:\Users\{username}\International Organization for Migration - IOM\HELIOS - Information Management\HELIOS Database\DB'
else:
    heliosdbPath = fr'C:\Users\{username}\International Organization for Migration - IOM\HELIOS - Documents{mitsiosPath}\Information Management\HELIOS Database\DB'
if username == 'gpolitis':
    contactsPath = fr'C:\Users\{username}\International Organization for Migration - IOM\HELIOS - Information Management\HELIOS Database\04 Contacts'
else:
    contactsPath = fr'C:\Users\{username}\International Organization for Migration - IOM\HELIOS - Documents{mitsiosPath}\Information Management\HELIOS Database\04 Contacts'

#Creating arrays in the same order, so that a simple loop can iterate through them and refresh/update the correct files on the correct forms
pathList = [accServicePath, matchMakingPath, monthlyDisbursementsPath, individualsPath, outreachV2Path, heliosdbPath, contactsPath]
fileList = ["accservice_csv", "mmaking_csv", "md_csv", "Individuals", "Outreach v2", "HELIOS Database v4", "Contacts"]
xformIDList = [975448, 1219842, 1159370]




#Window creation for the purpose of having 3 buttons to select which csv you want to refresh. Sample and unused code below
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# function to open a new window
# on a button click
def openNewWindow():
     
    # Toplevel object which will
    # be treated as a new window
    newWindow = Toplevel(master)
 
    # sets the title of the
    # Toplevel widget
    newWindow.title("New Window")
 
    # sets the geometry of toplevel
    newWindow.geometry("200x200")
 
    # A Label widget to show in toplevel
    Label(newWindow,
          text ="This is a new window").pack()
 
# creates a Tk() object
master = Tk()
# sets the geometry of main
# root window
master.geometry("200x200")
label = Label(master,
              text ="This is the main window")
 
label.pack(pady = 10)
# a button widget which will open a
# new window on button click
btn = Button(master,
             text ="Click to open a new window",
             command = openNewWindow)
btn.pack(pady = 10)
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

#Kill any excel process running at the moment. This is to avoid a fail in opening and already open file as this creates a loop of fails
def killExcel():
    for proc in psu.process_iter():
        if proc.name() == "EXCEL.EXE" or proc.name() == "excel.exe":
            proc.kill()
            time.sleep(2)
            
#x has a default "skip" value to skip kobo refresh & csv saving in case of non-csv file
def refreshCSV(p, f, x="skip"):
    #Refresh all Queries in a single file
    #triesRemaining = 100 #unused atm, purpose is to try 100 times to open each file, in order to make sure that it works even in slower machines
    failsafe = FALSE #invoked if an exception occurs and file processing will not consist after being refreshed+saved
    #while triesRemaining > 0: #loop for 100 openings. Add indent if used
    try:
        if x=='skip':
            print(f"Refreshing {f}.xlsx")
        else:
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
        if x == 'skip':
            print(f"{f}.xlsx was successfully saved")
        else:    
            read_file.to_csv(f"{p}\\{f}.csv", index = None, header = True, encoding="utf_8_sig")
            print(f"{f}.csv was successfully saved")
    except:
        #traceback.print_exc()
        #triesRemaining -= 1 #loop escape
        if wb is not None:
            del wb
        del xlapp
        killExcel() #kill all running excel instances
        failsafe = TRUE
        print(f"{f}.csv was NOT refreshed and was skipped")

    if x!='skip':
        if failsafe == FALSE:
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
    print("Returned to main menu")
    return 0

def main():
    #request = input("All excel processes currently running will be terminated for a successful running of the script. If you agree type 1. Otherwise type anything.")
    #if request == '1':
    #skip = 2 #basic skipping index, e.g. if 2, skips first 2 entries
    #index = -1
    killExcel()
    filesFullyRefreshed = 0 #used to see how many files were refreshed successfully

    #iterate through the list of files and refresh/update each one
    for i in range(len(pathList)):
        #index += 1
        #if skip == index:
        filesFullyRefreshed += refreshCSV(pathList[i], fileList[i], xformIDList[i]) #increment
    if filesFullyRefreshed == 3:
        print("All cool, bruh, all  files were refreshed")
    elif filesFullyRefreshed == 0:
        print("It hurts me in my black heart, but 0 refreshes unfortunately :(")
    else:
        print("Sad times bruh, " + str(filesFullyRefreshed) + " files were refreshed")

if __name__ == '__main__':
	main()