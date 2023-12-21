import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry  # Requires 'tkcalendar' package to be installed
from datetime import datetime

#used mainly in shift feedback
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
    day = date.strftime('%A') if date else ""
    day_var.set(day)
    usual_shift = usual_shift_combobox.get()

    # Perform any validation or data processing here
    # For simplicity, we will just display the entered data
    messagebox.showinfo("Shift Data Entered", f"Name: {name}\nShift: {shift}\nDate: {date}\nDay: {day}\nUsual Shift: {usual_shift}")

    # Close the shift input window
    shift_window.destroy()


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


def on_medicine_submit():
    global medicine_name_entry

    name = medicine_name_entry.get()

    # Perform any validation or data processing here
    # For simplicity, we will just display the entered data
    messagebox.showinfo("Medicine Data Entered", f"Name: {name}")

    # Close the medicine input window
    medicine_input_window.destroy()

def on_dog_submit():
    global dog_name_entry, arrival_date_entry, currently_fostered_var, times_fostered_entry

    if dog_name_entry is not None and arrival_date_entry is not None and currently_fostered_var is not None:
        name = dog_name_entry.get()
        arrival_date = arrival_date_entry.get()
        currently_fostered = currently_fostered_var.get()
        times_fostered = times_fostered_entry.get() if currently_fostered == "Yes" else ""

        # Perform any validation or data processing here
        # For simplicity, we will just display the entered data
        messagebox.showinfo("Dog Data Entered", f"Name: {name}\nDate of Arrival: {arrival_date}\nCurrently Fostered: {currently_fostered}\nTimes Fostered: {times_fostered}")

        # Close the dog input window
        dog_input_window.destroy()

    else:
        print("Dog input fields are not initialized.")

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
    global dog_name_entry, arrival_date_entry, currently_fostered_var, times_fostered_entry, dog_input_window

    # Create a new window for the dog input box
    dog_input_window = tk.Toplevel(root)
    dog_input_window.title("Add New Dog")

    # Create a frame to hold the input fields
    input_frame = ttk.Frame(dog_input_window, padding=20)
    input_frame.grid(row=0, column=0, sticky="nsew")

    # Labels
    name_label = ttk.Label(input_frame, text="Name:")
    name_label.grid(row=0, column=0, sticky="w")

    # Entry field for Dog Name
    dog_name_entry = ttk.Entry(input_frame, width=30)
    dog_name_entry.grid(row=0, column=1, padx=10, pady=5)

    # Date of Arrival Entry using 'tkcalendar'
    arrival_date_label = ttk.Label(input_frame, text="Date of Arrival:")
    arrival_date_label.grid(row=1, column=0, sticky="w")
    arrival_date_entry = DateEntry(input_frame, width=12, background='darkblue', foreground='white',
                                   borderwidth=2, year=2023, date_pattern='dd/mm/yyyy')
    arrival_date_entry.grid(row=1, column=1, padx=10, pady=5)

    # Currently Fostered Radioboxes
    global currently_fostered_var
    currently_fostered_var = tk.StringVar()
    currently_fostered_var.set("No")  # Set default selection to "No"
    currently_fostered_label = ttk.Label(input_frame, text="Currently Fostered:")
    currently_fostered_label.grid(row=2, column=0, sticky="w")
    fostered_yes_radio = ttk.Radiobutton(input_frame, text="Yes", variable=currently_fostered_var, value="Yes", command=on_currently_fostered_change)
    fostered_yes_radio.grid(row=2, column=1, padx=5)
    fostered_no_radio = ttk.Radiobutton(input_frame, text="No", variable=currently_fostered_var, value="No", command=on_currently_fostered_change)
    fostered_no_radio.grid(row=2, column=2, padx=5)

    # Times Fostered Entry
    global times_fostered_entry
    times_fostered_label = ttk.Label(input_frame, text="Times Fostered:")
    times_fostered_label.grid(row=3, column=0, sticky="w")
    times_fostered_entry = ttk.Entry(input_frame, width=5, state="readonly")
    times_fostered_entry.grid(row=3, column=1, padx=10, pady=5)

    # Submit button
    submit_button = ttk.Button(input_frame, text="Submit", command=on_dog_submit)
    submit_button.grid(row=4, column=0, columnspan=2, pady=10)

    # Return button
    return_button = ttk.Button(input_frame, text="Return", command=dog_input_window.destroy)
    return_button.grid(row=4, column=2, pady=10)

    # Adjust row and column weights to make the input fields expandable
    input_frame.columnconfigure((1, 2), weight=1)

def add_shift_feedback():
    global name_entry, shift_var, shift_date_entry, day_var, usual_shift_combobox, shift_window

    # Create a new window for the shift input box
    shift_window = tk.Toplevel(root)
    shift_window.title("Add Shift Feedback")
    shift_window.geometry("400x250")

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
    shift_day_combobox = ttk.Combobox(input_frame, values=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
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
"""
def add_shift():
    global name_entry, shift_var, shift_date_entry, day_var, usual_shift_combobox, shift_window

    # Create a new window for the shift input box
    shift_window = tk.Toplevel(root)
    shift_window.title("Add Shift Info")
    shift_window.geometry("400x250")

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
    usual_shift_combobox = ttk.Combobox(shift_frame, textvariable=usual_shift_var, values=["Yes", "No", "Tourist"])
    usual_shift_combobox.grid(row=4, column=1, columnspan=2, padx=10, pady=5)

    # Submit button
    submit_button = ttk.Button(shift_frame, text="Submit", command=on_shift_submit)
    submit_button.grid(row=5, column=0, columnspan=2, pady=10)

    # Return button
    return_button = ttk.Button(shift_frame, text="Return", command=shift_window.destroy)
    return_button.grid(row=5, column=2, pady=10)

    # Adjust row and column weights to make the input fields expandable
    shift_frame.columnconfigure((1, 2), weight=1)
"""
# Create the main window
root = tk.Tk()
root.title("Select what would you like to do")

action_frame = ttk.Frame(root, padding=20)
action_frame.grid(row=0, column=0, sticky="nsew")

# Add a shift button
shift_button = ttk.Button(action_frame, text="Shift Feedback", command=add_shift_feedback)
shift_button.grid(row=0, column=0, padx=10, pady=5)

# Add Volunteer button
volunteer_button = ttk.Button(action_frame, text="Add Volunteer", command=add_volunteer)
volunteer_button.grid(row=0, column=1, padx=10, pady=5)

# Add Volunteer Update button
volunteer_update_button = ttk.Button(action_frame, text="Add Volunteer Update", command=lambda: print("Add Volunteer Update button clicked"))
volunteer_update_button.grid(row=0, column=2, padx=10, pady=5)

# Add Dog Update button
dog_update_button = ttk.Button(action_frame, text="Add Dog Update", command=lambda: print("Add Dog Update button clicked"))
dog_update_button.grid(row=1, column=0, padx=10, pady=5)

# Add Dog button
dog_button = ttk.Button(action_frame, text="Add New Dog", command=show_dog_input_box)
dog_button.grid(row=1, column=1, padx=10, pady=5)

# Add Medicine button
medicine_button = ttk.Button(action_frame, text="Add Medicine", command=add_medicine)
medicine_button.grid(row=1, column=2, padx=10, pady=5)

action_frame.columnconfigure((0, 1, 2), weight=1)

# Create variables for shift input
name_entry = None
shift_var = None
shift_date_entry = None
day_var = tk.StringVar()
usual_shift_combobox = None
shift_window = None  # Variable to keep track of the shift input window

root.mainloop()