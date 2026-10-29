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

    csvDisplay = kin.Toplevel(tableDisplay)
    csvDisplay.title("CSV Table")
    csvDisplay.geometry("600x400")

    # Holds the table as its on section.
    tableWhole = kin.Frame(csvDisplay)
    tableWhole.pack(anchor="w", pady=(50, 0))

    tableSection = kin.Frame(tableWhole)
    tableSection.pack(side="left", anchor="nw")

    buttonHold = kin.Frame(tableDisplay)
    buttonHold.pack(side="left", anchor="n", padx=10)

    #Treeview table display and fills the window.
    tableColrow = t.Treeview(tableSection, show="headings", height=10)
    tableColrow.pack(anchor="nw")

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

    maxPages = m.ceil(maxRows / limiterRows)
    maxSets = m.ceil(maxColumns / limiterColumns)

    # Page number counter.
    pageCounter = kin.Label(buttonHold, text=f"Page 1 of {maxPages}")
    pageCounter.pack()

    # Sets counter.
    setCounter = kin.Label(buttonHold, text=f"Set 1 of {maxSets}")
    setCounter.pack()

    firColumn = 0
    endColumn = limiterColumns

    firSet = 0
    firPage = 0

    def clicks(selected):
        nonlocal firSet, firColumn, endColumn
        firSet = firSet + selected
        firSet = max(0, min(firSet, maxSets - 1))

        firColumn = firSet * limiterColumns
        endColumn = firColumn + limiterColumns
        setCounter.config(text=f"Set {firSet + 1} of {maxSets}")

        refreshContents()

    setLeft = kin.Button(buttonHold, text="<", command=lambda: clicks(-1))
    setLeft.pack(side="left")

        
    setRight = kin.Button(buttonHold, text=">", command=lambda: clicks(1))
    setRight.pack(side="left")



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

        startRow = 0
        endRow = limiterRows

        # Adds the rows to the table.
        for dataRows in rowStarters[startRow:endRow]:
            tableColrow.insert("", "end", values = dataRows[firColumn:endColumn])


    refreshContents()
    tableDisplay.mainloop()