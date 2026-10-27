import tkinter as kin
from tkinter import filedialog as fd

# filedialog will be used later for CSV.

# kin.Tk allows creates the main window.
# .title sets the name in the bar.
# .geometry sets the width and height for the display.
mainDisplay = kin.Tk()
mainDisplay.title("Data Analyzer")
mainDisplay.geometry("1000x600")

# Creations of the Main Title.
# Shows at the top centered.
# .label creates a label in the display.
# .pack positions where that label goes.
# Using pady to make a title appear on the top of the screen.
title = kin.Label(mainDisplay, text= "Data Analyzer", font=("Courier New", 30, "bold"))
title.pack(pady = 10)

# .Frame creates a frame in mainDisplay.
# positions the notification in the center.
notifMessage = kin.Frame(mainDisplay)
notifMessage.pack(fill="x", padx=15)

# We add a bracket for decoration to hold the message
# on the left side.
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

# multipleTabs is a main frame that holds the entire section
# with the three boxes.
# it expands to fill the available space with expand=True.
# padx and pady add space around the frame.
multipleTabs = kin.Frame(mainDisplay)
multipleTabs.pack(fill="both", expand=True, padx=25, pady=(220,10))

# Now we add a frame inside multipleTabs that holds
# three independent boxes.
# x represents being placed on the left side edge.
# y represents being pushed down from the top
# relwidth fills the width set to 1
# relheight uses the full height set to 1
# We subtract 30 to offset from the 30 space at the top.
descBoxes = kin.Frame(multipleTabs)
descBoxes.place(x=0, y=30, relwidth=1, relheight=1, height=-30)

# columnconfigure allows us to set the grid
# 0 starts, weight of 1 to fill, and uniform with the other boxes
# copy and pasted for the other 2 sections.
# weight can have more space if set on 2 or 0 for no extra space.
descBoxes.columnconfigure(0, weight=1, uniform="infoBoxes")
descBoxes.columnconfigure(1, weight=1, uniform="infoBoxes")
descBoxes.columnconfigure(2, weight=1, uniform="infoBoxes")

# This is for the left box.
# Since we've been working with 225 we set height to 225.
# borderwidth sets the thickness.
# relief gives borders a solid look.
# .grid gives positioning.
# row set to 0, top or starting position.
# column set to 0,  leftmost or starting position.
# nsew means north, south, east, west
# this just expands the box on all corners.
leftBox = kin.Frame(descBoxes, height = 225, borderwidth = 1, relief = "solid")
leftBox.grid(row = 0, column = 0, sticky="nsew")

# repeated for middle box.
midBox = kin.Frame(descBoxes, height = 225, borderwidth = 1, relief = "solid")
midBox.grid(row = 0, column = 1, sticky="nsew")

# repeated for right box.
rightBox = kin.Frame(descBoxes, height = 225, borderwidth = 1, relief = "solid")
rightBox.grid(row = 0, column = 2, sticky="nsew")

# Allows to stretch vertically with the available height.
descBoxes.rowconfigure(0, weight=1)

# .mainloop allows the window to be open.
mainDisplay.mainloop()