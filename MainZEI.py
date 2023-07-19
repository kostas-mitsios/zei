import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry  # Requires 'tkcalendar' package to be installed

name_entry = None
time_var = None
date_var = None
listbox = None
data_input_window = None  # Variable to keep track of the data input window

def on_submit():
    global name_entry, time_var, date_var, listbox

    if name_entry is not None and time_var is not None and date_var is not None and listbox is not None:
        name = name_entry.get()
        morning_or_afternoon = time_var.get()
        chosen_date = date_var.get()
        last_selections = listbox.curselection()
        selected_options = [listbox.get(index) for index in last_selections]

        # Perform any validation or data processing here
        # For simplicity, we will just display the entered data
        messagebox.showinfo("Data Entered", f"Name: {name}\nTime: {morning_or_afternoon}\nDate: {chosen_date}\nMedication(s): {', '.join(selected_options)}")

        # Close the data input window
        data_input_window.destroy()

    else:
        print("Data input fields are not initialized.")

def on_action_selected(action):
    if action == "Add a shift":
        # Code for adding a shift
        print("Adding a shift")
        # Put your code here to add a shift

        # Call the function to show the data input box
        show_data_input_box()

def show_data_input_box():
    global name_entry, time_var, date_var, listbox, data_input_window

    # Create a new window for the data input box
    data_input_window = tk.Toplevel(root)
    data_input_window.title("Data Input Box")

    # Create a frame to hold the input fields
    input_frame = ttk.Frame(data_input_window, padding=20)
    input_frame.grid(row=0, column=0, sticky="nsew")

    # Labels
    name_label = ttk.Label(input_frame, text="Name:")
    name_label.grid(row=0, column=0, sticky="w")

    # Entry field for Name
    name_entry = ttk.Entry(input_frame, width=30)
    name_entry.grid(row=0, column=1, padx=10, pady=5)

    # Time (Morning or Afternoon) Radioboxes
    time_var = tk.StringVar()
    time_var.set("morning")  # Set default selection to "morning"
    time_label = ttk.Label(input_frame, text="Time:")
    time_label.grid(row=1, column=0, sticky="w")
    morning_radio = ttk.Radiobutton(input_frame, text="Morning", variable=time_var, value="morning")
    morning_radio.grid(row=1, column=1, padx=5)
    afternoon_radio = ttk.Radiobutton(input_frame, text="Afternoon", variable=time_var, value="afternoon")
    afternoon_radio.grid(row=1, column=2, padx=5)

    # Date Entry using 'tkcalendar'
    date_label = ttk.Label(input_frame, text="Date:")
    date_label.grid(row=2, column=0, sticky="w")
    date_var = tk.StringVar()
    date_entry = DateEntry(input_frame, width=12, background='darkblue', foreground='white',
                           borderwidth=2, year=2023, date_pattern='dd/mm/yyyy', textvariable=date_var)
    date_entry.grid(row=2, column=1, padx=10, pady=5)

    # Dropdown List with multiple options
    dropdown_label = ttk.Label(input_frame, text="Medication(s):")
    dropdown_label.grid(row=3, column=0, sticky="w")
    options = ["Xozal", "Augmentin", "Flexadin"]
    listbox = tk.Listbox(input_frame, selectmode='multiple', exportselection=0)
    for option in options:
        listbox.insert(tk.END, option)
    listbox.grid(row=3, column=1, padx=10, pady=5)

    # Submit button
    submit_button = ttk.Button(input_frame, text="Submit", command=on_submit)
    submit_button.grid(row=4, column=0, columnspan=2, pady=10)

    # Return button
    return_button = ttk.Button(input_frame, text="Return", command=data_input_window.destroy)
    return_button.grid(row=4, column=2, pady=10)

    # Adjust row and column weights to make the input fields expandable
    input_frame.columnconfigure((1, 2), weight=1)

# Create the main window
root = tk.Tk()
root.title("Select waht would you like to do")

# Create a frame to hold the action buttons
action_frame = ttk.Frame(root, padding=20)
action_frame.grid(row=0, column=0, sticky="nsew")

# Add a shift button
shift_button = ttk.Button(action_frame, text="Add a shift", command=lambda: on_action_selected("Add a shift"))
shift_button.grid(row=0, column=0, padx=10, pady=5)

# Other buttons (For simplicity, we'll set them to do nothing)
ttk.Button(action_frame, text="Add a new dog", command=lambda: on_action_selected("Add a new dog")).grid(row=0, column=1, padx=10, pady=5)
ttk.Button(action_frame, text="Remove a dog", command=lambda: on_action_selected("Remove a dog")).grid(row=0, column=2, padx=10, pady=5)
ttk.Button(action_frame, text="Add a medication", command=lambda: on_action_selected("Add a medication")).grid(row=0, column=3, padx=10, pady=5)

# Adjust row and column weights to make the action frame expandable
action_frame.columnconfigure((0, 1, 2, 3), weight=1)

# Start the main event loop
root.mainloop()
