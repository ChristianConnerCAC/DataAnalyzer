import tkinter as kin
from tkinter import ttk as t
import math as m

#Displays the second screen called "Table View"
#Geometry matches with DA.py
#CSV connected
def tableView(tableStored, limiterRows, limiterColumns):
    tableDisplay = kin.Tk()
    tableDisplay.title("Table View")
    tableDisplay.geometry("1000x600")

    # Creates another window to fix an issue I couldn't solve.
    csvDisplay = kin.Toplevel(tableDisplay)
    csvDisplay.title("CSV Table")
    csvDisplay.geometry("600x400")

    # Holds the table in its own section.
    tableWhole = kin.Frame(csvDisplay)
    tableWhole.pack(anchor="w", pady=(50, 0))


    #Treeview table display and fills the window.
    tableColrow = t.Treeview(tableWhole, show="headings", height=10)
    tableColrow.pack(anchor="nw")

    # This holds buttons for the command screen
    infoSection = kin.Frame(tableDisplay)
    infoSection.pack(anchor="w", padx=6, pady=6)

    # Command Box to type in for commands
    infoBox = kin.Text(infoSection, bg="white", height=10, width=50)
    infoBox.pack()

    # Holds Buttons as their own section.
    buttonHold = kin.Frame(infoSection)
    buttonHold.pack(side="left", anchor="n", pady=10)

    setHold = kin.Frame(buttonHold)
    setHold.pack(side="left", padx=5)

    pageHold = kin.Frame(buttonHold)
    pageHold.pack(side="left", padx=5)

    # This sees if we have the CSV data.
    # Grabs data for rows and columns.
    # A row needs to appear first.
    if tableStored:
        colHeaders = tableStored[0]
        rowStarters = tableStored[1:]
    else:
        # If no rows and columns are available.
        colHeaders = []
        rowStarters = []

    # Sets a limit
    maxRows = len(rowStarters)
    maxColumns = len(colHeaders)

    # Uses .ceil to make sure they are whole
    maxPages = m.ceil(maxRows / limiterRows)
    maxSets = m.ceil(maxColumns / limiterColumns)

    # Page number counter.
    pageCounter = kin.Label(pageHold, text=f"Page 1 of {maxPages}")
    pageCounter.pack()

    # Sets counter.
    setCounter = kin.Label(setHold, text=f"Set 1 of {maxSets}")
    setCounter.pack()

    # Sets the positions for start and end of columns.
    firColumn = 0
    endColumn = limiterColumns

    # Tracks the counts for columns and rows.
    firSet = 0
    firPage = 0

    # Both use non local since they will be using variables
    # outside their definitions.
    # made a few adjustments.
    def pageClicks(selected):
        nonlocal firPage
        firPage = firPage + selected
        firPage = max(0, min(firPage, maxPages - 1))

        pageCounter.config(text=f"Page {firPage + 1} of {maxPages}")

        refreshContents()

    # Displays correct clicks on buttons
    def setClicks(selected):
        nonlocal firSet, firColumn, endColumn
        firSet = firSet + selected
        firSet = max(0, min(firSet, maxSets - 1))

        firColumn = firSet * limiterColumns
        endColumn = firColumn + limiterColumns
        setCounter.config(text=f"Set {firSet + 1} of {maxSets}")

        refreshContents()

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



    # Refreshes the contents for sets
    def refreshContents():
        displayHeaders = colHeaders[firColumn:endColumn]

        # Number of columns into a list.
        numColumns = limiterColumns
        amtColumns = range(numColumns)
        listTable = list(amtColumns)

        # Sets them into a table
        tableColrow["columns"] = listTable

        # Starts at 0
        # Displays columns heading and width
        # Moves columns over to the next.
        startAt = 0
        for each in displayHeaders:
            tableColrow.heading(startAt, text=each)
            tableColrow.column(startAt, width=60, minwidth=60)
            startAt = startAt + 1

        for displayed in tableColrow.get_children():
            tableColrow.delete(displayed)

        startRow = firPage * limiterRows
        endRow = startRow + limiterRows

        # Adds the rows to the table.
        for dataRows in rowStarters[startRow:endRow]:
            tableColrow.insert("", "end", values = dataRows[firColumn:endColumn])


    refreshContents()
    tableDisplay.mainloop()