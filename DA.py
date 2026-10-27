import tkinter as kin
from tkinter import filedialog as fd

# kin.Tk allows creates the main window
# .title sets the name in the bar
# .geometry sets the width and height for the display.
mainDisplay = kin.Tk()
mainDisplay.title("Data Analyzer")
mainDisplay.geometry("1000x600")

# Creations of the Main Title
# Shows at the top centered
# .label creates a label in the display.
# .pack positions where that label goes.
# Using pady to make a title appear on the top of the screen.
title = kin.Label(mainDisplay, text= "Data Analyzer", font=("Courier New", 30, "bold"))
title.pack(pady = 10)

# .Frame creates a frame in mainDisplay
# positions the notification in the center.
notifMessage = kin.Frame(mainDisplay)
notifMessage.pack(fill="x", padx=15)

# We add a bracket for decoration to hold the message
# on the left side
leftBrkt = kin.Label(notifMessage, text="[", font=("Courier New", 35))
leftBrkt.pack(side="left")

# The Contents inside the left and right brackets
# Centered to make sure it stays between the brackets
# Using \n to not overflow into the brackets
# Starts the message on the left side.
insideNotif = kin.Label(
    notifMessage,
    text = "Welcome to the Data Analyzer, please either hover over \n"
            "Create Table, Load CSV, or Load Template down below for more information",
    font = ("Courier New", 15),
    justify = "center"
)
insideNotif.pack(side="left", padx=5)

# The right side bracket decoration to hold the message
rightBrkt = kin.Label(notifMessage, text="]", font=("Courier New", 35))
rightBrkt.pack(side="right")

# .mainloop allows the window to be open.
mainDisplay.mainloop()