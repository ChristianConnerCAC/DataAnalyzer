import tkinter as kin
from tkinter import ttk as t

# Displays the second screen called "Table View"
# Geometry matches with DA.py
# CSV connected
def tableView(tableStored):
    tableDisplay = kin.Tk()
    tableDisplay.title("Table View")
    tableDisplay.geometry("1000x600")


    tableWhole = kin.Frame(tableDisplay)
    tableWhole.pack(anchor="w", pady=(120))
    
    # Treeview table display and fills the window
    tableColrow = t.Treeview(tableWhole, show="headings")
    tableColrow.pack(anchor="w")

    # Page number counter
    pageCounter = kin.Label(tableWhole, text="Page 1 of 1")
    pageCounter.pack(anchor="e")

    # Sets counter
    setCounter = kin.Label(tableWhole, text="Set 1 of 1")
    setCounter.pack(anchor="w")

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
    # Number of columns into a list.
    numColumns = len(colHeaders)
    amtColumns = range(numColumns)
    listTable = list(amtColumns)
    # Sets them into a table and starts at index 0.
    tableColrow["columns"] = listTable
    startAt = 0

    # Displays columns heading and width
    # Moves columns over to the next.
    for each in colHeaders:
        tableColrow.heading(startAt, text=each)
        tableColrow.column(startAt, width=150)
        startAt = startAt + 1

    # Adds the rows to the table.
    for dataRows in rowStarters:
        tableColrow.insert("", "end", values = dataRows)



    tableDisplay.mainloop()