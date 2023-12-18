import time
import tkinter as tk
from tkinter import *
from tkinter import ttk
from datetime import datetime
from win10toast import ToastNotifier  # Import ToastNotifier for notifications
import winsound  # Import winsound for sound

# Create the window
window = Tk()
window.geometry('600x400')  # Adjusted height for a more compact layout
window.title('Countdown Timer')

# Initialize Tkinter variables
hour = StringVar()
minus = StringVar()
secon = StringVar()
check = BooleanVar()
count = IntVar()

# Function to start the countdown
def countdown():
    # Get the time values from the entry fields
    hours = int(hour.get())
    minutes = int(minus.get())
    seconds = int(secon.get())

    # Convert everything to seconds
    total_seconds = hours * 3600 + minutes * 60 + seconds

    while total_seconds:
        mins, secs = divmod(total_seconds, 60)
        display = '{:02d}:{:02d}'.format(mins, secs)
        time.sleep(1)
        total_seconds -= 1
        label_var.set(display)  # Update label text dynamically
        window.update()  # Update the window to display changes

    label_var.set("Time-Up")

    # Display notification on desktop
    toast = ToastNotifier()
    toast.show_toast("Notification", "Timer is Off", duration=20, icon_path=None, threaded=True)

    if check.get():
        winsound.Beep(440, 1000)

# Label to display the countdown
label_var = StringVar()
countdown_label = Label(window, textvariable=label_var, font=('Helvetica', 20, 'bold'))
countdown_label.pack(pady=20)  # Added padding for better spacing

# Other UI elements with styling
entry_style = ttk.Style()
entry_style.configure('TEntry', padding=(5, 5, 5, 5))  # Added padding to entry widgets

Label(window, text="Enter time in HH:MM:SS", font=('Helvetica', 12, 'bold')).pack(pady=10)
Entry(window, textvariable=hour, font=('Helvetica', 12)).pack()
Entry(window, textvariable=minus, font=('Helvetica', 12)).pack()
Entry(window, textvariable=secon, font=('Helvetica', 12)).pack()

Checkbutton(text='Check for Music', onvalue=True, variable=check, font=('Helvetica', 12)).pack(pady=10)

Button(window, text="Set Countdown", command=countdown, bg='#FFD700', font=('Helvetica', 12, 'bold')).place(x=230, y=320)

# To print the current time
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
Label(window, text=current_time, font=('Helvetica', 12)).pack()

# Run the main loop
window.mainloop()
