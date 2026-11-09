import tkinter as kin
import math as m
import guidance

# total amount for pages and sets for navigation.
def totalNavi(maxRows, maxColumns, limiterColumns, limiterRows):
    # Uses .ceil to make sure they are whole
    maxPages = max(1, m.ceil(maxRows / limiterRows))
    maxSets = max(1, m.ceil (maxColumns / limiterColumns))
    return maxPages, maxSets

# Both use non local since they will be using variables
# outside their definitions.
# made a few adjustments.
def pageClicks(selected, firPage, maxPages):
    firPage = firPage + selected
    firPage = max(0, min(firPage, maxPages - 1))
    return firPage

# Displays correct clicks on buttons
def setClicks(selected, firSet, limiterColumns, maxSets):
    firSet = firSet + selected
    firSet = max(0, min(firSet, maxSets - 1))

    firColumn = firSet * limiterColumns
    endColumn = firColumn + limiterColumns
    return firSet, firColumn, endColumn

def buttonNavi(pageClicks, pageHold, maxPages, maxSets, setHold, setClicks):
    # Page number counter.
    # Changed the formats from previous versions to accomodate for naviHover guidance
    pageTitle = kin.Frame(pageHold)
    pageTitle.pack()

    pageHover = kin.Label(pageTitle, text="Page", font=("Courier New", 12, "bold", "underline"), foreground="green")
    pageHover.pack(side="left")

    pageCounter = kin.Label(pageTitle, text=f"1 of {maxPages}")
    pageCounter.pack(side="left")

    guidance.naviHover("Shows pages (of 10 max) of rows\n"
                       "to be displayed per page.", pageHover)

    # Sets counter.
    setTitle = kin.Frame(setHold)
    setTitle.pack()

    setHover = kin.Label(setTitle, text="Set", font=("Courier New", 12, "bold", "underline"), foreground="green")
    setHover.pack(side="left")

    setCounter = kin.Label(setTitle, text=f"1 of {maxSets}")
    setCounter.pack(side="left")

    guidance.naviHover("Shows a set (of 10 max) of columns\n"
                       "to be displayed per set.", setHover)

    # Left and Right buttons for Sets to click over.
    setLeft = kin.Button(setHold, text="<", command=lambda: setClicks(-1))
    setLeft.pack(side="left")

        
    setRight = kin.Button(setHold, text=">", command=lambda: setClicks(1))
    setRight.pack(side="left")

    # Copy pasted sets for pages.
    pageLeft = kin.Button(pageHold, text="<", command=lambda: pageClicks(-1))
    pageLeft.pack(side="left")

        
    pageRight = kin.Button(pageHold, text=">", command=lambda: pageClicks(1))
    pageRight.pack(side="left")

    return pageCounter, setCounter