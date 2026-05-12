#Study Session Tracker App
#This app allows users to log study sessions by subject and time, view all sessions,
#and see total study time. Users can also clear all sessions.

#-----------------Sources I have Used ------------------
#Source 1: GitHub - Simple Calculator using Tkinter
#https://github.com/raunakroy2810/Simplest_calculator/blob/main/Simple%20calculator.py
#Source 2: Github - Python Log Manager
#https://github.com/Aman-pr/python_log_manger/blob/main/log_manager_gui.py
from tkinter import *
# Tkinter is Python's standard GUI library.
# The '*' imports all Tkinter classes and functions so we can use them directly (e.g., Tk(), Button, Entry, Label).

# ------------------- Borrowed / Modified -------------------
root = Tk()
#Borrowed from Simple Calculator GUI
# Creates the main window object for the application. This window is where all GUI elements will appear.
root.title("Study Session Tracker")
# Modified from Simple Calculator GUI
# .title() sets the title text that appears on the top bar of the main window.

root.geometry("450x450")
# Borrowed from Log Manager GUI
# .geometry() sets the width and height of the main window in pixels (450 wide, 450 tall).

# ------------------- Original Code -----------------------
subject_entry = Entry(root, width=35, borderwidth=5)
# Creates a single-line text entry widget for the subject name.
# 'width=35' controls the horizontal size of the entry box.
# 'borderwidth=5' adds a border around the entry for better visibility.

subject_entry.grid(row=0, column=1, padx=10, pady=5)
# Places the entry box in the GUI using a grid layout.
# 'row' and 'column' define its position in a grid.
# padx/pady add horizontal/vertical spacing around the widget.

time_entry = Entry(root, width=35, borderwidth=5)
# Creates a single-line text entry widget for time studied (in hours).

time_entry.grid(row=1, column=1, padx=10, pady=5)
# Places the time entry box on the grid below the subject entry.

subject_label = Label(root, text="Subject:")
# Creates a label widget with the text 'Subject:' to indicate the subject entry box.
#Label() creates a text label.
subject_label.grid(row=0, column=0)
# Places the label to the left of the subject_entry using the grid system.

time_label = Label(root, text="Time Studied (hours):")
# Creates a label to indicate the time_entry box.

time_label.grid(row=1, column=0)
# Places the label to the left of the time_entry using grid.

result_label = Label(root, text="", justify="left")
# Creates a label that will dynamically display all study sessions.
# 'justify="left"' aligns multiple lines of text to the left.

result_label.grid(row=4, column=0, columnspan=3, pady=10)
# columnspan=3 makes this label stretch across 3 columns.
# pady=10 adds vertical spacing above and below.
sessions = []
# Initializes an empty Python list to store tuples of (subject, hours studied).

# ------------------- Original Functions -------------------
def add_session():
    # Function to add a study session when the "Add Session" button is clicked.
    subject = subject_entry.get()
    # .get() retrieves the current text from the subject_entry widget.

    time = time_entry.get()
    #  .get() retrieves the current text from the time_entry widget.

    if subject and time:
        # Checks that both fields are not empty.
        try:
            time_float = float(time)
            # Converts the entered time to a float. Raises ValueError if not a number.
            sessions.append((subject, time_float))
            # Adds a tuple of (subject, hours) to the sessions list.
            display_sessions()
            # Calls display_sessions() to update the result_label with all sessions.
            subject_entry.delete(0, END)
            # Clears the subject_entry box for the next input.
            # .delete(0, END) clears the text in the Entry widget from position 0 to end.
            time_entry.delete(0, END)
            # Clears the time_entry box.
        except ValueError:
            result_label.config(text="Please enter a valid number for time!")
            # Shows an error message if the time entered is not a valid number.
            # .config() changes widget properties dynamically (here, updates label text).
    else:
        result_label.config(text="Please enter both subject and time!")
        # Shows an error message if either field is empty.

def display_sessions():
    # Function to update the result_label with all study sessions and total time.
    text = ""
    # Temporary string to store formatted session data.
    total_time = 0
    # Variable to calculate total hours studied.

    for s in sessions:
        # Loops through all tuples in the sessions list.
        text += f"{s[0]}: {s[1]} hours\n"
        # Adds each session to the text string.
        total_time += s[1]
        # Adds the hours to total_time.

    text += f"\nTotal Study Time: {total_time} hours"
    # Adds total study time at the end of the text.

    result_label.config(text=text)
    # Updates the result_label widget with the new text.

def clear_sessions():
    # Function to clear all study sessions.
    sessions.clear()
    # Removes all items from the sessions list.
    display_sessions()
    # Updates the GUI to show an empty list.

# ------------------- Borrowed / Modified Buttons -------------------
add_button = Button(root, text="Add Session", padx=40, pady=20, command=add_session, bg="#4CAF50", fg="white")
# Borrowed & Modified from Simple Calculator GUI (button layout and colors customized)
# Button() creates a clickable button labeled "Add Session".
# 'command=add_session' runs the add_session function when clicked.
# 'bg' and 'fg' set background and text color.
# 'padx' and 'pady' control button size padding.

add_button.grid(row=2, column=0, columnspan=3, pady=5)
# Borrowed & Modified from Simple Calculator GUI
# Places the button on the grid and spans 3 columns for width.

clear_button = Button(root, text="Clear All", padx=40, pady=20, command=clear_sessions, bg="#F44336", fg="white")
# Borrowed & Modified from Simple Calculator GUI
# Creates a button to clear all sessions.

clear_button.grid(row=3, column=0, columnspan=3, pady=5)
# Borrowed & Modified from Simple Calculator GUI
# Places the "Clear All" button below the Add Session button.

# ------------------- Borrowed -------------------
root.mainloop()
# Borrowed from both Simple Calculator and Log Manager GUI
# Starts the Tkinter event loop.
# This keeps the window open and listens for user interactions (button clicks, text entry, etc.).