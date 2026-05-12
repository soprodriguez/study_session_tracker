# Study Session Tracker App (Python GUI)

## Description

This project is a Study Session Tracker application built using Python and Tkinter. It allows users to log study sessions by entering a subject and the number of hours studied. The app displays all recorded sessions and calculates the total study time.

Users can also clear all sessions with a single button, making it easy to manage and reset their study logs.

## Features

* Add study sessions by subject and hours
* Display all sessions in a list format
* Automatically calculate total study time
* Input validation for numeric time values
* Clear all sessions with one click
* Simple and user-friendly GUI

## Technologies Used

* **Python**
* **tkinter** (for GUI development)

## Requirements

* Python installed on your system
* tkinter (comes pre-installed with most Python distributions)

## How to Run the Program

1. Save the code in a Python file (e.g., `study_tracker.py`).
2. Open your terminal or IDE.
3. Run the program:

   ```
   python study_tracker.py
   ```
4. Enter a subject and the number of hours studied.
5. Click **"Add Session"** to log the session.
6. View all sessions and total study time displayed in the app.
7. Click **"Clear All"** to reset all sessions.

## Example Usage

* Input:

  * Subject: Math
  * Time: 2

* Output:

  ```
  Math: 2.0 hours

  Total Study Time: 2.0 hours
  ```

## Notes

* The program stores sessions in a list during runtime (data is not saved after closing the app).
* Input validation ensures that time is entered as a number.
* This project is useful for learning GUI design, data handling, and user input validation in Python.
