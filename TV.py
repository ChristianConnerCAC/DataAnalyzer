import tkinter as kin
from tkinter import ttk as t
import time
import guidance

# Sort allows the ascending and descending of the table.
import sort
# Search allows the search bar, buttons and search table to work.
import search
# TVnavi is for navigation like buttons
import TVnavi
# Command Bar Rules
import command

#Rearrange to look nicer later
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
    csvDisplay.geometry("800x400")

    # Holds the table in its own section.
    tableWhole = kin.Frame(csvDisplay)
    tableWhole.pack(anchor="w", pady=(50, 0))


    #Treeview table display and fills the window.
    # Height determines how many rows are seen.
    # Tree headings displays both for treeview
    tableColrow = t.Treeview(tableWhole, show="tree headings", height=10)
    tableColrow.pack(anchor="nw")

    tableColrow.heading("#0", text="")
    tableColrow.column("#0", width=40, stretch=False)

    # This holds buttons for the command screen
    infoSection = kin.Frame(tableDisplay)
    infoSection.pack(anchor="w", padx=6, pady=6)

    # Command Box to type in for commands
    infoBox = kin.Text(infoSection, bg="white", height=20, width=110)
    infoBox.pack()

    # Holds search bar as their own section
    searchHold =kin.Frame(infoSection)
    searchHold.pack(anchor="w", pady=6)

    # Search Bar to find information
    searchSelection = kin.Entry(searchHold, width= 50)
    searchSelection.pack(side="left")

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

    # Allows to update the table with new information
    # Takes those updates rows and columns
    # Counts the rows and columns
    # Updates the total pages and sets then refreshes.
    def entryUpdate():
        nonlocal maxPages, maxSets, maxRows, maxColumns, rowStarters, colHeaders
        colHeaders = tableStored[0]
        rowStarters = tableStored[1:]
        maxRows = len(rowStarters)
        maxColumns = len(colHeaders)
        maxPages, maxSets = TVnavi.totalNavi(maxRows, maxColumns, limiterColumns, limiterRows)
        refreshContents()

    # Sets a limit
    maxRows = len(rowStarters)
    maxColumns = len(colHeaders)
    maxPages, maxSets = TVnavi.totalNavi(maxRows, maxColumns, limiterColumns, limiterRows)

    # Sets the positions for start and end of columns.
    firColumn = 0
    endColumn = limiterColumns

    # Tracks the counts for columns and rows.
    firSet = 0
    firPage = 0


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
        # Allows columns to have numbers to read easier.
        startAt = 0
        for each in displayHeaders:
            if firColumn + startAt in sortedDirection:
                if sortedDirection[firColumn + startAt] == True:
                    sortText = " (Asc)"
                else:
                    sortText = " (Des)"
            else:
                sortText = ""
            tableColrow.heading(startAt, text=f"({startAt + firColumn + 1}) {each}{sortText}", command = lambda a=firColumn + startAt: sortedCols(a))
            tableColrow.column(startAt, width=75, minwidth=70)
            startAt = startAt + 1

        for displayed in tableColrow.get_children():
            tableColrow.delete(displayed)

        startRow = firPage * limiterRows
        endRow = startRow + limiterRows

        # Adds the rows to the table.
        # Allows for rows to have their own numbers to easily read
        for dataRows in rowStarters[startRow:endRow]:
            tableColrow.insert("", "end", text=f"({startRow + 1})", values = dataRows[firColumn:endColumn])
            startRow = startRow + 1

    # Sorting direction for columns
    sortedDirection = {}

    # User Story Sort
    # Clears the asc and des.
    # Selected columns get sorted
    def sortedCols(column):
        for click in list(sortedDirection):
            if click != column:
                del sortedDirection[click]
        sort.sortedCols(rowStarters, column, sortedDirection)
        # Uses this function to update the table.
        refreshContents()

    # This allows search bar to find data in the table
    # by typing into the search bar and
    # if nothing in entered it returns nothing.
    def searchData():
        findData = searchSelection.get().lower()
        if not findData:
            return
        search.searchData(tableDisplay, rowStarters, colHeaders, limiterRows, limiterColumns, findData)
    
    # use nonlocal since they will be using variables
    # outside their definitions.
    # made a few adjustments.
    # We use nonlocal because if it was in the definitions it
    # would reset to 0 everytime.
    def pageClicks(selected):
        nonlocal firPage
        firPage = TVnavi.pageClicks(selected, firPage, maxPages)
        pageCounter.config(text=f"Page {firPage + 1} of {maxPages}")
        refreshContents()

    # Displays correct clicks on button
    # This moves through the sets and columns instead of pages.
    def setClicks(selected):
        nonlocal firSet, firColumn, endColumn
        firSet, firColumn, endColumn = TVnavi.setClicks(selected, firSet, limiterColumns, maxSets)
        setCounter.config(text=f"{firSet + 1} of {maxSets}")
        refreshContents()

    # Search button to be able to search.
    searchButton = kin.Button(searchHold, text="Search", command=searchData, font=("Courier New", 12, "bold", "underline"), foreground="green")
    searchButton.pack(side="left")

    guidance.naviHover("Allows the user to search for\n"
                       "specific information within the table.", searchButton)

    def closeTable():
        tableDisplay.destroy()

    # Allows for the page and set counters and buttons.
    pageCounter, setCounter = TVnavi.buttonNavi(pageClicks, pageHold, maxPages, maxSets, setHold, setClicks)

    # We imported time to pass a non-func test
    # This tests how fast they load
    nonFunc2 = time.perf_counter()
    refreshContents()
    endFunc2 = time.perf_counter()
    calcFunc2 = endFunc2 - nonFunc2
    infoBox.see("end")

    command.helpCommand(infoBox, tableStored, entryUpdate, closeTable, calcFunc2)
    
    tableDisplay.mainloop()