import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import Calendar
from tkcalendar import DateEntry  # Requires 'tkcalendar' package to be installed
from PIL import Image, ImageTk
from datetime import datetime

def calculate_day(event=None):
    selected_date = shift_date_entry.get_date()
    if selected_date:
        selected_day = selected_date.strftime('%A')
        day_var.set(selected_day)

def on_shift_feedback_submit():
    global name_entry, shift_var, shift_date_entry, day_var, usual_shift_combobox

    name = name_entry.get()
    shift = shift_var.get()
    date = shift_date_entry.get()
    if date:
        date = datetime.strptime(date, "%d/%m/%Y")
        day = date.strftime("%A")
    else:
        day = ""
    date = str(date.strftime("%d/%m/%Y"))
    #day = date.strftime('%A') if date else ""
    day_var.set(day)
    usual_shift = usual_shift_combobox.get()

    # Perform any validation or data processing here
    # For simplicity, we will just display the entered data
    messagebox.showinfo("Shift Data Entered", f"Name: {name}\nShift: {shift}\nDate: {date}\nDay: {day}\nUsual Shift: {usual_shift}")

    # Close the shift input window
    shift_window.destroy()

    #openSelectedSheet("Shifts")
    data_to_write = [
    [name, date, day, shift, usual_shift]
    ]

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
    worksheet = sheet.worksheet("Shifts")
    next_empty_row = len(worksheet.col_values(1)) + 1
    worksheet.insert_rows(data_to_write, next_empty_row)  # You can specify the row number where data should be inserted


def on_volunteer_submit():
    global volunteer_name_entry, date_started_entry, date_stopped_entry, shift_day_combobox, shift_time_var, tourist_checkbox

    name = volunteer_name_entry.get()
    date_started = date_started_entry.get()
    date_stopped = date_stopped_entry.get()
    shift_day = shift_day_combobox.get()
    shift_time = shift_time_var.get()
    tourist = "Yes" if tourist_var.get() else "No"

    # Perform any validation or data processing here
    # For simplicity, we will just display the entered data
    messagebox.showinfo("Volunteer Data Entered", f"Name: {name}\nDate Started: {date_started}\nDate Stopped: {date_stopped}\nUsual Shift Day: {shift_day}\nUsual Shift Time: {shift_time}\nTourist: {tourist}")

    # Close the volunteer input window
    volunteer_input_window.destroy()
    
    data_to_write = [
    [name, date_started, date_stopped, shift_day, shift_time, tourist]
    ]

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
    worksheet = sheet.worksheet("Volunteers")
    next_empty_row = len(worksheet.col_values(1)) + 1
    worksheet.insert_rows(data_to_write, next_empty_row)  # You can specify the row number where data should be inserted

def on_volunteer_updated_submit():
    ""

def on_medicine_submit():
    global medicine_name_entry

    medicationName = medicine_name_entry.get()

    # Perform any validation or data processing here
    # For simplicity, we will just display the entered data
    messagebox.showinfo("Medicine Data Entered", f"Name: {medicationName}")

    # Close the medicine input window
    medicine_input_window.destroy()

    data_to_write = [
    [medicationName]
    ]

    # Define your credentials file path
    credentials_file = 'credentials.json'

    # Authenticate with Google Sheets API
    scope = ["https://www.googleapis.com/auth/spreadsheets"]
    credentials = service_account.Credentials.from_service_account_file(credentials_file, scopes=scope)
    client = gspread.Client(auth=credentials)

    # Open the Google Sheet by its ID
    sheet_id = "1sm_ePXHiTxty5gHfgW_rWGhzdnml1G6sVfuwKfKWeMM"
    sheet = client.open_by_key(sheet_id)

    # Select the "Medications" sheet by its title
    worksheet = sheet.worksheet("Medications")
    next_empty_row = len(worksheet.col_values(1)) + 1
    worksheet.insert_rows(data_to_write, next_empty_row)  # You can specify the row number where data should be inserted

def on_dog_submit():
    global name_entry, arrival_date_entry, currently_fostered_var, times_fostered_entry

    if name_entry is not None and arrival_date_entry is not None and currently_fostered_var is not None:
        name = name_entry.get()
        arrival_date = arrival_date_entry.get()
        currently_fostered = currently_fostered_var.get()
        times_fostered = times_fostered_entry.get() if currently_fostered == "Yes" else ""

        # Perform any validation or data processing here
        # For simplicity, we will just display the entered data
        messagebox.showinfo("Dog Data Entered", f"Name: {name}\nDate of Arrival: {arrival_date}\nCurrently Fostered: {currently_fostered}\nTimes Fostered: {times_fostered}")

        # Close the dog input window
        input_window.destroy()

    else:
        print("Dog input fields are not initialized.")

def on_cat_submit():
    global name_entry, arrival_date_entry, currently_fostered_var, times_fostered_entry

    if name_entry is not None and arrival_date_entry is not None and currently_fostered_var is not None:
        name = name_entry.get()
        arrival_date = arrival_date_entry.get()
        currently_fostered = currently_fostered_var.get()
        times_fostered = times_fostered_entry.get() if currently_fostered == "Yes" else ""

        # Perform any validation or data processing here
        # For simplicity, we will just display the entered data
        messagebox.showinfo("Dog Data Entered", f"Name: {name}\nDate of Arrival: {arrival_date}\nCurrently Fostered: {currently_fostered}\nTimes Fostered: {times_fostered}")

        # Close the dog input window
        input_window.destroy()

    else:
        print("Cat input fields are not initialized.")
#tbd
def on_currently_fostered_change():
    global currently_fostered_var, times_fostered_entry

    if currently_fostered_var.get() == "Yes":
        times_fostered_entry.config(state="normal")
        times_fostered_entry.delete(0, tk.END)
        times_fostered_entry.insert(0, "1")
    else:
        times_fostered_entry.delete(0, tk.END)
        times_fostered_entry.config(state="readonly")

def show_dog_input_box():
    global name_entry, arrival_date_entry, currently_fostered_var, times_fostered_entry, input_window
    global years_spinbox, months_spinbox

    # Create a new window for the dog input box
    input_window = tk.Toplevel(root)
    input_window.title("Add New Dog")
    input_window.iconbitmap("zeil_logo.ico")

    # Create a frame to hold the input fields
    input_frame = ttk.Frame(input_window, padding=20)
    input_frame.grid(row=0, column=0, sticky="nsew")

    # Labels
    name_label = ttk.Label(input_frame, text="Name:")
    name_label.grid(row=0, column=0, sticky="w")

    # Entry field for Dog Name
    name_entry = ttk.Entry(input_frame, width=30)
    name_entry.grid(row=0, column=1, padx=10, pady=5)

    # Date of Arrival Entry using 'tkcalendar'
    arrival_date_label = ttk.Label(input_frame, text="Date of Arrival:")
    arrival_date_label.grid(row=1, column=0, sticky="w")
    arrival_date_entry = DateEntry(input_frame, width=12, background='darkblue', foreground='white',
                                   borderwidth=2, year=2023, date_pattern='dd/mm/yyyy')
    arrival_date_entry.grid(row=1, column=1, padx=10, pady=5)

    # Currently Fostered Radioboxes
    currently_fostered_var = tk.StringVar()
    currently_fostered_var.set("No")  # Set default selection to "No"
    currently_fostered_label = ttk.Label(input_frame, text="Currently Fostered:")
    currently_fostered_label.grid(row=2, column=0, sticky="w")
    fostered_yes_radio = ttk.Radiobutton(input_frame, text="Yes", variable=currently_fostered_var, value="Yes", command=on_currently_fostered_change)
    fostered_yes_radio.grid(row=2, column=1, padx=5)
    fostered_no_radio = ttk.Radiobutton(input_frame, text="No", variable=currently_fostered_var, value="No", command=on_currently_fostered_change)
    fostered_no_radio.grid(row=2, column=2, padx=5)

    # Years and Months Spinboxes
    years_label = ttk.Label(input_frame, text="Years:")
    years_label.grid(row=3, column=0, sticky="w")
    years_spinbox = ttk.Spinbox(input_frame, from_=0, to=20)
    years_spinbox.grid(row=3, column=1, padx=10, pady=5)

    months_label = ttk.Label(input_frame, text="Months:")
    months_label.grid(row=4, column=0, sticky="w")
    months_spinbox = ttk.Spinbox(input_frame, from_=0, to=12)
    months_spinbox.grid(row=4, column=1, padx=10, pady=5)

    # Times Fostered Entry
    times_fostered_label = ttk.Label(input_frame, text="Times Fostered:")
    times_fostered_label.grid(row=5, column=0, sticky="w")
    times_fostered_entry = ttk.Entry(input_frame, width=5, state="readonly")
    times_fostered_entry.grid(row=5, column=1, padx=10, pady=5)

    # Submit button
    submit_button = ttk.Button(input_frame, text="Submit", command=on_dog_submit)
    submit_button.grid(row=6, column=0, columnspan=2, pady=10)

    # Return button
    return_button = ttk.Button(input_frame, text="Return", command=input_window.destroy)
    return_button.grid(row=6, column=2, pady=10)

    # Adjust row and column weights to make the input fields expandable
    input_frame.columnconfigure((1, 2), weight=1)

#tbd
def on_dog_update_submit():
    ""

#tbd
def on_cat_update_submit():
    ""

#tbd
def show_cat_input_box():
    global name_entry, arrival_date_entry, currently_fostered_var, times_fostered_entry, input_window
    global years_spinbox, months_spinbox

    # Create a new window for the dog input box
    input_window = tk.Toplevel(root)
    input_window.title("Add New Cat")
    input_window.iconbitmap("zeil_logo.ico")

    # Create a frame to hold the input fields
    input_frame = ttk.Frame(input_window, padding=20)
    input_frame.grid(row=0, column=0, sticky="nsew")

    # Labels
    name_label = ttk.Label(input_frame, text="Name:")
    name_label.grid(row=0, column=0, sticky="w")

    # Entry field for Dog Name
    name_entry = ttk.Entry(input_frame, width=30)
    name_entry.grid(row=0, column=1, padx=10, pady=5)

    # Date of Arrival Entry using 'tkcalendar'
    arrival_date_entry_label = ttk.Label(input_frame, text="Date of Arrival:")
    arrival_date_entry_label.grid(row=1, column=0, sticky="w")
    arrival_date_entry = DateEntry(input_frame, width=12, background='darkblue', foreground='white',
                                   borderwidth=2, year=2023, date_pattern='dd/mm/yyyy')
    arrival_date_entry_label.grid(row=1, column=1, padx=10, pady=5)

    # Currently Fostered Radioboxes
    currently_fostered_var = tk.StringVar()
    currently_fostered_var.set("No")  # Set default selection to "No"
    currently_fostered_var_label = ttk.Label(input_frame, text="Currently Fostered:")
    currently_fostered_var_label.grid(row=2, column=0, sticky="w")
    #tdb maybe command to change to cat specific. Same to dog
    fostered_yes_radio = ttk.Radiobutton(input_frame, text="Yes", variable=currently_fostered_var, value="Yes", command=on_currently_fostered_change)
    fostered_yes_radio.grid(row=2, column=1, padx=5)
    #tdb maybe command to change to cat specific. Same to dog
    fostered_no_radio = ttk.Radiobutton(input_frame, text="No", variable=currently_fostered_var, value="No", command=on_currently_fostered_change)
    fostered_no_radio.grid(row=2, column=2, padx=5)

    # Years and Months Spinboxes
    years_label = ttk.Label(input_frame, text="Years:")
    years_label.grid(row=3, column=0, sticky="w")
    years_spinbox = ttk.Spinbox(input_frame, from_=0, to=20)
    years_spinbox.grid(row=3, column=1, padx=10, pady=5)

    months_label = ttk.Label(input_frame, text="Months:")
    months_label.grid(row=4, column=0, sticky="w")
    months_spinbox = ttk.Spinbox(input_frame, from_=0, to=12)
    months_spinbox.grid(row=4, column=1, padx=10, pady=5)

    # Times Fostered Entry
    times_fostered_label = ttk.Label(input_frame, text="Times Fostered:")
    times_fostered_label.grid(row=5, column=0, sticky="w")
    times_fostered_entry = ttk.Entry(input_frame, width=5, state="readonly")
    times_fostered_entry.grid(row=5, column=1, padx=10, pady=5)

    # Submit button
    submit_button = ttk.Button(input_frame, text="Submit", command=on_cat_submit)
    submit_button.grid(row=6, column=0, columnspan=2, pady=10)

    # Return button
    return_button = ttk.Button(input_frame, text="Return", command=input_window.destroy)
    return_button.grid(row=6, column=2, pady=10)

    # Adjust row and column weights to make the input fields expandable
    input_frame.columnconfigure((1, 2), weight=1)



def add_shift():
    global name_entry, shift_var, shift_date_entry, day_var, usual_shift_combobox, shift_window

    # Create a new window for the shift input box
    shift_window = tk.Toplevel(root)
    shift_window.title("Add Shift Feedback")
    shift_window.geometry("400x250")
    shift_window.iconbitmap("zeil_logo.ico")

    shift_frame = ttk.Frame(shift_window, padding=20)
    shift_frame.pack(fill=tk.BOTH, expand=True)

    # Labels
    name_label = ttk.Label(shift_frame, text="Volunteer submitting feedback:")
    name_label.grid(row=0, column=0, sticky="w")

    shift_label = ttk.Label(shift_frame, text="Shift:")
    shift_label.grid(row=1, column=0, sticky="w")

    date_label = ttk.Label(shift_frame, text="Date of Shift:")
    date_label.grid(row=2, column=0, sticky="w")

    day_label = ttk.Label(shift_frame, text="Day:")
    day_label.grid(row=3, column=0, sticky="w")

    #probably to remove this button #todo
    usual_shift_label = ttk.Label(shift_frame, text="Usual Shift:")
    usual_shift_label.grid(row=4, column=0, sticky="w")

    # Entry fields
    name_entry = ttk.Entry(shift_frame, width=30)
    name_entry.grid(row=0, column=1, columnspan=2, padx=10, pady=5)

    # Shift Radioboxes
    shift_var = tk.StringVar()
    shift_var.set("Morning")  # Set default selection to "Morning"
    morning_radio = ttk.Radiobutton(shift_frame, text="Morning", variable=shift_var, value="Morning")
    morning_radio.grid(row=1, column=1, padx=5)
    afternoon_radio = ttk.Radiobutton(shift_frame, text="Afternoon", variable=shift_var, value="Afternoon")
    afternoon_radio.grid(row=1, column=2, padx=5)

    # Date Entry using 'tkcalendar'
    #calendar starts at current year
    shift_date_entry = DateEntry(shift_frame, width=12, background='darkblue', foreground='white',
                                 borderwidth=2, year=2023, date_pattern='dd/mm/yyyy')
    shift_date_entry.grid(row=2, column=1, columnspan=2, padx=10, pady=5)

    # Bind the DateEntrySelected event to the calculate_day function
    shift_date_entry.bind("<<DateEntrySelected>>", calculate_day)
    #messagebox.showinfo("shift date: ", calculate_day)

    # Day Entry (Readonly)
    day_var = tk.StringVar()
    day_entry = ttk.Entry(shift_frame, textvariable=day_var, state="readonly")
    day_entry.grid(row=3, column=1, columnspan=2, padx=10, pady=5)

    # Usual Shift Dropdown
    usual_shift_var = tk.StringVar()
    usual_shift_combobox = ttk.Combobox(shift_frame, textvariable=usual_shift_var, values=["Yes", "No", "Tourist"])
    usual_shift_combobox.grid(row=4, column=1, columnspan=2, padx=10, pady=5)

    # Submit button
    submit_button = ttk.Button(shift_frame, text="Submit", command=on_shift_feedback_submit)
    submit_button.grid(row=5, column=1, pady=10)

    # Return button
    return_button = ttk.Button(shift_frame, text="Return", command=shift_window.destroy)
    return_button.grid(row=5, column=2, pady=10)

    # Adjust row and column weights to make the input fields expandable
    shift_frame.columnconfigure((1, 2), weight=1)

def add_volunteer():
    global volunteer_name_entry, date_started_entry, date_stopped_entry, shift_day_combobox, shift_time_var, tourist_var, volunteer_input_window

    # Create a new window for the volunteer input box
    volunteer_input_window = tk.Toplevel(root)
    volunteer_input_window.title("Add Volunteer")
    volunteer_input_window.iconbitmap("zeil_logo.ico")

    # Create a frame to hold the input fields
    input_frame = ttk.Frame(volunteer_input_window, padding=20)
    input_frame.grid(row=0, column=0, sticky="nsew")

    # Labels
    name_label = ttk.Label(input_frame, text="Name:")
    name_label.grid(row=0, column=0, sticky="w")

    date_started_label = ttk.Label(input_frame, text="Date Started:")
    date_started_label.grid(row=1, column=0, sticky="w")

    date_stopped_label = ttk.Label(input_frame, text="Date Stopped:")
    date_stopped_label.grid(row=2, column=0, sticky="w")

    shift_day_label = ttk.Label(input_frame, text="Usual Shift Day:")
    shift_day_label.grid(row=3, column=0, sticky="w")

    shift_time_label = ttk.Label(input_frame, text="Usual Shift Time:")
    shift_time_label.grid(row=4, column=0, sticky="w")

    tourist_label = ttk.Label(input_frame, text="Tourist:")
    tourist_label.grid(row=5, column=0, sticky="w")

    # Entry fields
    volunteer_name_entry = ttk.Entry(input_frame, width=30)
    volunteer_name_entry.grid(row=0, column=1, padx=10, pady=5)

    # Date Started Entry using 'tkcalendar'
    date_started_entry = DateEntry(input_frame, width=12, background='darkblue', foreground='white',
                                   borderwidth=2, year=2023, date_pattern='dd/mm/yyyy')
    date_started_entry.grid(row=1, column=1, padx=10, pady=5)

    # Date Stopped Entry using 'tkcalendar'
    date_stopped_entry = DateEntry(input_frame, width=12, background='darkblue', foreground='white',
                                   borderwidth=2, year=2023, date_pattern='dd/mm/yyyy')
    date_stopped_entry.grid(row=2, column=1, padx=10, pady=5)

    # Usual Shift Day Combobox
    shift_day_combobox = ttk.Combobox(input_frame, values=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], state="readonly")
    shift_day_combobox.grid(row=3, column=1, padx=10, pady=5)

    # Usual Shift Time Radioboxes
    shift_time_var = tk.StringVar()
    shift_time_var.set("Morning")  # Set default selection to "Morning"
    morning_radio = ttk.Radiobutton(input_frame, text="Morning", variable=shift_time_var, value="Morning")
    morning_radio.grid(row=4, column=1, padx=5)
    afternoon_radio = ttk.Radiobutton(input_frame, text="Afternoon", variable=shift_time_var, value="Afternoon")
    afternoon_radio.grid(row=4, column=2, padx=5)

    # Tourist Checkbox
    tourist_var = tk.BooleanVar()
    tourist_checkbox = ttk.Checkbutton(input_frame, variable=tourist_var)
    tourist_checkbox.grid(row=5, column=1, padx=10, pady=5)

    # Submit button
    submit_button = ttk.Button(input_frame, text="Submit", command=on_volunteer_submit)
    submit_button.grid(row=6, column=0, columnspan=2, pady=10)

    # Return button
    return_button = ttk.Button(input_frame, text="Return", command=volunteer_input_window.destroy)
    return_button.grid(row=6, column=2, pady=10)

    # Adjust row and column weights to make the input fields expandable
    input_frame.columnconfigure((1, 2), weight=1)

def add_medicine():
    global medicine_name_entry, medicine_input_window

    # Create a new window for the medicine input box
    medicine_input_window = tk.Toplevel(root)
    medicine_input_window.title("Add Medicine")
    medicine_input_window.iconbitmap("zeil_logo.ico")

    # Create a frame to hold the input fields
    input_frame = ttk.Frame(medicine_input_window, padding=20)
    input_frame.grid(row=0, column=0, sticky="nsew")

    # Labels
    name_label = ttk.Label(input_frame, text="Name:")
    name_label.grid(row=0, column=0, sticky="w")

    # Entry field for Medicine Name
    medicine_name_entry = ttk.Entry(input_frame, width=30)
    medicine_name_entry.grid(row=0, column=1, padx=10, pady=5)

    # Submit button
    submit_button = ttk.Button(input_frame, text="Submit", command=on_medicine_submit)
    submit_button.grid(row=1, column=0, columnspan=2, pady=10)

    # Return button
    return_button = ttk.Button(input_frame, text="Return", command=medicine_input_window.destroy)
    return_button.grid(row=1, column=2, pady=10)

    # Adjust row and column weights to make the input fields expandable
    input_frame.columnconfigure((1, 2), weight=1)

def show_info(cal):
    selected_date = cal.get_date()
    info = get_data_for_date(selected_date)
    
    if info:
        display_info(selected_date, info)
    else:
        display_info(selected_date, "No data found for this date.")

def get_data_for_date(selected_date):
    # Authenticate with Google Sheets API using your credentials
    credentials_file = 'credentials.json'
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    credentials = service_account.Credentials.from_service_account_file(credentials_file, scopes=scope)
    client = gspread.Client(auth=credentials)
    
    # Open the Google Sheet by its ID
    sheet_id = "1sm_ePXHiTxty5gHfgW_rWGhzdnml1G6sVfuwKfKWeMM"
    worksheet = client.open_by_key(sheet_id).worksheet("Volunteers")
    
    # Fetch all data from column B
    column_b_data = worksheet.col_values(2)
    
    # Collect all rows with matching dates
    matching_rows = []

    for i, date in enumerate(column_b_data):
        if date == selected_date:
            row_with_date = worksheet.row_values(i + 1)  # Adjust for 0-based indexing
            matching_rows.append(row_with_date)

    formatted_data_list = []
    
    for row in matching_rows:
        formatted_data = '\n'.join([f"{label}: {value}" for label, value in zip(labels, row)])
        formatted_data_list.append(formatted_data)

    # Join the formatted data with newlines to get a single string
    formatted_data_string = '\n\n'.join(formatted_data_list)

    return formatted_data_string

def display_info(selected_date, info):
    info_window = tk.Toplevel(root)
    info_window.title("Information")
    info_window.iconbitmap("zeil_logo.ico")
    
    info_text = tk.Text(info_window, wrap=tk.WORD)
    info_text.pack(padx=10, pady=10)

    info_text.insert(tk.END, f"Data for {selected_date}:\n\n{''.join(info)}")

    # Set the color for the words in the labels
    for label in labels:
        start = info_text.search(label, "1.0", stop=tk.END)
        end = f"{start}+{len(label)}c"
        info_text.tag_add(label, start, end)
        info_text.tag_config(label, foreground="blue")  # Change the color here

def show_calendar():
    root = tk.Tk()
    root.title("Calendar")
    root.iconbitmap("zeil_logo.ico")

    # Create a Calendar widget
    cal = Calendar(root, date_pattern="dd/mm/y")
    cal.pack(padx=10, pady=10)

    # Create a frame to organize the buttons
    button_frame = tk.Frame(root)
    button_frame.pack(pady=10)

    # Button to show information for the selected date
    show_info_button = tk.Button(button_frame, text="Show Info", command=lambda: show_info(cal))
    show_info_button.pack(side="left", padx=10)

    # Button to return and close the window
    return_button = tk.Button(button_frame, text="Return", command=root.destroy)
    return_button.pack(side="left", padx=10)

def show_inventory():
    global view_inventory, add_inventory_item, edit_inventory, inventory_menu_window

    # Create a new window for the inventory menu
    inventory_menu_window = tk.Toplevel(root)
    inventory_menu_window.title("Inventory Menu")
    inventory_menu_window.iconbitmap("zeil_logo.ico")

    # Create a frame to hold the input fields
    input_frame = ttk.Frame(inventory_menu_window, padding=20)
    input_frame.grid(row=0, column=0, sticky="nsew")

    # View inventory button
    view_inventory_button = ttk.Button(input_frame, text="View Inventory", command=on_view_inventory_submit)
    view_inventory_button.grid(row=1, column=0, columnspan=1, pady=10)


    # Return button
    return_button = ttk.Button(input_frame, text="Return", command=inventory_menu_window.destroy)
    return_button.grid(row=3, column=0, pady=10)

    # Adjust row and column weights to make the input fields expandable
    input_frame.columnconfigure((0), weight=1)

#tbd
def on_view_inventory_submit():
    ""
#tbd
def show_donations_menu():
    global donations_menu_window

    # Create a new window for the donations menu
    donations_menu_window = tk.Toplevel(root)
    donations_menu_window.title("Donations Menu")
    donations_menu_window.configure(bg='blue')
    donations_menu_window.iconbitmap("zeil_logo.ico")

    # Create a custom style for blue buttons
    style = ttk.Style()
    style.configure("Blue.TButton", foreground="black", background="red")

    # Create a frame to hold the input fields
    input_frame = ttk.Frame(donations_menu_window, padding=20)
    input_frame.grid(row=0, column=0, sticky="nsew")

    # View inventory button
    view_donations_button = ttk.Button(input_frame, text="View Donations", command=on_view_donations, style="Blue.TButton")
    view_donations_button.grid(row=1, column=0, columnspan=1, pady=10)

    # View inventory button
    add_donation_button = ttk.Button(input_frame, text="Add Donations", command=on_add_donations)
    add_donation_button.grid(row=1, column=2, columnspan=1, pady=10)

    # Return button
    return_button = ttk.Button(input_frame, text="Return", command=donations_menu_window.destroy)
    return_button.grid(row=2, column=1, pady=10)

    # Adjust row and column weights to make the input fields expandable
    input_frame.columnconfigure((1, 2), weight=1)

#tbd
def on_view_donations():
    # Create a new window for the donations menu
    donations_view_window = tk.Toplevel(root)
    donations_view_window.title("All Donations")
    donations_view_window.configure(bg='green')
    donations_view_window.iconbitmap("zeil_logo.ico")
    #tbd

def on_add_donations():
    global donor_name, donation_date, donation_items

    # Create a new window for the add donation menu
    donation_add_window = tk.Toplevel(root)
    donation_add_window.title("Add Donation")
    donation_add_window.configure(bg='green')
    donation_add_window.iconbitmap("zeil_logo.ico")

    # Create a frame to hold the input fields
    input_frame = ttk.Frame(donation_add_window, padding=20)
    input_frame.grid(row=0, column=0, sticky="nsew")

    # Labels
    donor_label = ttk.Label(input_frame, text="Donor:")
    donor_label.grid(row=0, column=0, sticky="w")

    donation_date_label = ttk.Label(input_frame, text="Date:")
    donation_date_label.grid(row=1, column=0, sticky="w")

    donation_items_label = ttk.Label(input_frame, text="Items")
    donation_items_label.grid(row=2, column=0, sticky="w")
    
    donor_name = ttk.Entry(input_frame, width=30)
    donor_name.grid(row=0, column=1, padx=10, pady=5)

    donation_date = DateEntry(input_frame, width=12, background='darkblue', foreground='white',
                                   borderwidth=2, year=2023, date_pattern='dd/mm/yyyy')
    donation_date.grid(row=1, column=1, padx=10, pady=5)

    donation_items = ttk.Entry(input_frame, width=30)
    donation_items.grid(row=2, column=1, padx=10, pady=5)

    # Submit donation button
    submit_donation_button = ttk.Button(input_frame, text="Submit", command=on_add_donations_submit)
    submit_donation_button.grid(row=4, column=0, columnspan=1, pady=10)

    # Return button
    return_button = ttk.Button(input_frame, text="Return", command=donation_add_window.destroy)
    return_button.grid(row=4, column=2, pady=10)
    
    # Adjust row and column weights to make the input fields expandable
    input_frame.columnconfigure((0, 1, 2), weight=1)
    
def on_add_donations_submit():
    donor = donor_name.get()
    date = donation_date.get()
    items = donation_items.get()

    data_to_write = [
    [donor, date, items]
    ]

    # Define your credentials file path
    credentials_file = 'credentials.json'

    # Authenticate with Google Sheets API
    scope = ["https://www.googleapis.com/auth/spreadsheets"]
    credentials = service_account.Credentials.from_service_account_file(credentials_file, scopes=scope)
    client = gspread.Client(auth=credentials)

    # Open the Google Sheet by its ID
    sheet_id = "1sm_ePXHiTxty5gHfgW_rWGhzdnml1G6sVfuwKfKWeMM"

    try:
        sheet = client.open_by_key(sheet_id)
    except APIError as e:
        print("API Error:", e)
    except Exception as e:
        print("An error occurred:", e)

    # Select the "Medications" sheet by its title
    worksheet = sheet.worksheet("Donations")
    next_empty_row = len(worksheet.col_values(1)) + 1
    worksheet.insert_rows(data_to_write, next_empty_row)  # You can specify the row number where data should be inserted

def add_shift():
    global name_entry, shift_var, shift_date_entry, day_var, usual_shift_combobox, shift_window

    # Create a new window for the shift input box
    shift_window = tk.Toplevel(root)
    shift_window.title("Add Shift Info")
    shift_window.geometry("400x250")
    shift_window.iconbitmap("zeil_logo.ico")

    shift_frame = ttk.Frame(shift_window, padding=20)
    shift_frame.pack(fill=tk.BOTH, expand=True)

    # Labels
    name_label = ttk.Label(shift_frame, text="Name:")
    name_label.grid(row=0, column=0, sticky="w")

    shift_label = ttk.Label(shift_frame, text="Shift:")
    shift_label.grid(row=1, column=0, sticky="w")

    date_label = ttk.Label(shift_frame, text="Date:")
    date_label.grid(row=2, column=0, sticky="w")

    day_label = ttk.Label(shift_frame, text="Day:")
    day_label.grid(row=3, column=0, sticky="w")

    usual_shift_label = ttk.Label(shift_frame, text="Usual Shift:")
    usual_shift_label.grid(row=4, column=0, sticky="w")

    # Entry fields
    name_entry = ttk.Entry(shift_frame, width=30)
    name_entry.grid(row=0, column=1, columnspan=2, padx=10, pady=5)

    # Shift Radioboxes
    shift_var = tk.StringVar()
    shift_var.set("Morning")  # Set default selection to "Morning"
    morning_radio = ttk.Radiobutton(shift_frame, text="Morning", variable=shift_var, value="Morning")
    morning_radio.grid(row=1, column=1, padx=5)
    afternoon_radio = ttk.Radiobutton(shift_frame, text="Afternoon", variable=shift_var, value="Afternoon")
    afternoon_radio.grid(row=1, column=2, padx=5)

    # Date Entry using 'tkcalendar'
    shift_date_entry = DateEntry(shift_frame, width=12, background='darkblue', foreground='white',
                                 borderwidth=2, year=2023, date_pattern='dd/mm/yyyy')
    shift_date_entry.grid(row=2, column=1, columnspan=2, padx=10, pady=5)

    # Bind the DateEntrySelected event to the calculate_day function
    shift_date_entry.bind("<<DateEntrySelected>>", calculate_day)

    # Day Entry (Readonly)
    day_var = tk.StringVar()
    day_entry = ttk.Entry(shift_frame, textvariable=day_var, state="readonly")
    day_entry.grid(row=3, column=1, columnspan=2, padx=10, pady=5)

    # Usual Shift Dropdown
    usual_shift_var = tk.StringVar()
    usual_shift_combobox = ttk.Combobox(shift_frame, textvariable=usual_shift_var, values=["Yes", "No", "Tourist"], state="readonly")
    usual_shift_combobox.grid(row=4, column=1, columnspan=2, padx=10, pady=5)

    # Submit button
    submit_button = ttk.Button(shift_frame, text="Submit", command=on_shift_submit)
    submit_button.grid(row=5, column=0, columnspan=2, pady=10)

    # Return button
    return_button = ttk.Button(shift_frame, text="Return", command=shift_window.destroy)
    return_button.grid(row=5, column=2, pady=10)

    # Adjust row and column weights to make the input fields expandable
    shift_frame.columnconfigure((1, 2), weight=1)

#tbd
def add_vet():
    ""

#tbd
def add_vet_visit():
    ""

#tbd
def add_incident():
    ""

def report_menu():
    ""

"""
def resize_image(event):
    # Resize the image to match the size of the frame
    new_width = event.width
    new_height = event.height
    image = original_image.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)
    label.configure(image=photo)
    label.image = photo  # Keep a reference
"""

# Create the main window
root = tk.Tk()
root.title("Select what would you like to do")
#Not resizable main window
root.resizable(False, False)
#root.configure(bg="blue")

# Load an image
#original_image = Image.open("zeil_logo.png")  # Replace "your_image.png" with your image file

# Set the theme
ttk.Style().theme_use('winnative')

# Create a style and configure the background color
style = ttk.Style()
style.configure('My.TFrame', background='green')  # Change 'blue' to your desired color
# Create a custom style for the red button
style = ttk.Style()
style.configure('Red.TButton', background='red', foreground='black')  # Set background to red and text color to white


root.iconbitmap("zeil_logo.ico")

action_frame = ttk.Frame(root, padding=20, style='My.TFrame')
action_frame.grid(row=0, column=0, sticky="nsew")

# Bind the frame to the resize_image function to handle window resizing
#action_frame.bind("<Configure>", resize_image)

# Create a label for the background image
#photo = ImageTk.PhotoImage(original_image)
#label = ttk.Label(action_frame, image=photo)
#label.place(relwidth=1, relheight=1)  # Stretch the label to fill the frame

# Add Shift button
shift_button = ttk.Button(action_frame, text="Shift Feedback", command=add_shift_feedback, style = 'Red.TButton')
shift_button.grid(row=0, column=0, padx=10, pady=5)

# Add Volunteer button
volunteer_button = ttk.Button(action_frame, text="Add Volunteer", command=add_volunteer, style = 'Red.TButton')
volunteer_button.grid(row=0, column=1, padx=10, pady=5)

# Add Volunteer Update button
volunteer_update_button = ttk.Button(action_frame, text="Add Volunteer Update", command=on_volunteer_updated_submit, style = 'Red.TButton')
volunteer_update_button.grid(row=0, column=2, padx=10, pady=5)

# Add New Dog button
dog_button = ttk.Button(action_frame, text="Add New Dog", command=show_dog_input_box, style = 'Red.TButton')
dog_button.grid(row=1, column=0, padx=10, pady=5)

# Add Dog Update button
dog_update_button = ttk.Button(action_frame, text="Add Dog Update", command=on_dog_update_submit, style = 'Red.TButton')
dog_update_button.grid(row=1, column=1, padx=10, pady=5)

# Add New Cat button
medicine_button = ttk.Button(action_frame, text="Add New Cat", command=show_cat_input_box, style = 'Red.TButton')
medicine_button.grid(row=1, column=2, padx=10, pady=5)

# Add Cat Update button
dog_update_button = ttk.Button(action_frame, text="Add Cat Update", command=on_cat_update_submit, style = 'Red.TButton')
dog_update_button.grid(row=1, column=3, padx=10, pady=5)

# Add Show Inventory button
medicine_button = ttk.Button(action_frame, text="Show Inventory", command=show_inventory, style = 'Red.TButton')
medicine_button.grid(row=2, column=0, padx=10, pady=5)

# Add Medicine button
medicine_button = ttk.Button(action_frame, text="Add Medicine", command=add_medicine, style = 'Red.TButton')
medicine_button.grid(row=2, column=1, padx=10, pady=5)

# Add Donations Menu button
medicine_button = ttk.Button(action_frame, text="Show Donations Menu", command=show_donations_menu, style = 'Red.TButton')
medicine_button.grid(row=2, column=2, padx=10, pady=5)

# Add Calendar button
shift_button = ttk.Button(action_frame, text="View Calendar", command=show_calendar, style = 'Red.TButton')
shift_button.grid(row=2, column=3, padx=10, pady=5)

# Add Vet button
shift_button = ttk.Button(action_frame, text="Add Vet", command=add_vet, style = 'Red.TButton')
shift_button.grid(row=3, column=0, padx=10, pady=5)

# Add Vet Visit button
shift_button = ttk.Button(action_frame, text="Vet Visit", command=add_vet_visit, style = 'Red.TButton')
shift_button.grid(row=3, column=1, padx=10, pady=5)

# Add Incident button
shift_button = ttk.Button(action_frame, text="Add Incident", command=add_incident, style = 'Red.TButton')
shift_button.grid(row=3, column=2, padx=10, pady=5)

# Add Report Menu Button
report_menu_button = ttk.Button(action_frame, text="Report Menu", command=report_menu, style = 'Red.TButton', width=35)
report_menu_button.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

action_frame.columnconfigure((0, 1, 2, 3), weight=1)

# Create variables for shift input
name_entry = None
arrival_date_entry = None
shift_var = None
shift_date_entry = None
day_var = tk.StringVar()
usual_shift_combobox = None
shift_window = None  # Variable to keep track of the shift input window

root.mainloop()