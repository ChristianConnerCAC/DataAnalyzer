import tkinter as kin
import math as m

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
    pageCounter = kin.Label(pageHold, text=f"Page 1 of {maxPages}")
    pageCounter.pack()

    # Sets counter.
    setCounter = kin.Label(setHold, text=f"Set 1 of {maxSets}")
    setCounter.pack()

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