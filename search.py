import tkinter as kin
from tkinter import ttk as t
import math as m
import sort
import guidance

# Allows data to be found in the search bar
# Checks each row for an exact match and returns that row.
def searchRows(rowStarters, findData):
    # searches exact matches
    obtainRows = [
        oRows for oRows in rowStarters
        if any(
            findData == str(theValues).lower()
            for theValues in oRows
        )
    ]
    return obtainRows

# Separate window is created for the search.
# Allows for set and page movement.
# Refreshes that page if needed.
def searchData(tableDisplay, rowStarters, colHeaders, limiterRows, limiterColumns, findData):
    obtainRows = searchRows(rowStarters, findData)
    # Seperate sortedDirection than TV so it doesnt affect the other.
    sortedDirection = {}

    # Creates a window to display the gathered information.
    searchDisplay = kin.Toplevel(tableDisplay)
    searchDisplay.title("Search Results")
    searchDisplay.geometry("800x400")

    # Table it its own section.
    searchAll = kin.Frame(searchDisplay)
    searchAll.pack(anchor="w")

    searchButton = kin.Frame(searchDisplay)
    searchButton.pack(anchor="w", pady=6)

    # Same thing we did with the normal set and pages.
    # Using .ceil from math to round.
    searchPages = max(1, m.ceil(len(obtainRows) / limiterRows))
    searchSets = max(1, m.ceil(len(colHeaders) / limiterColumns))

    # Nested function variables.
    searchPage = 0
    searchSet = 0

    # Defines the page clicks in the search results.
    # Moves through the pages of search results
    # Doesn't allow movement over or under the amount
    def searchPageClicks(selected):
        nonlocal searchPage
        searchPage = searchPage + selected
        searchPage = max(0, min(searchPage, searchPages - 1))
        searchPCounter.config(text=f"Page {searchPage + 1} of {searchPages}")
        refreshSearch()

    # Copy and pasted from searchPageClicks and adjusted,
    # Defines the set clicks in the search results.
    # This moves through the columns.
    def searchSetClicks(selected):
        nonlocal searchSet
        searchSet = searchSet + selected
        searchSet = max(0, min(searchSet, searchSets - 1))
        searchSCounter.config(text=f"Set {searchSet + 1} of {searchSets}")
        refreshSearch()

    # Sets the counter for pages and buttons for left and right,
    # inside the search results.
    searchPCounter = kin.Label(searchButton, text=f"Page 1 of {searchPages}")
    searchPCounter.pack(side="left")

    searchPageLeft = kin.Button(searchButton, text="<", command =lambda: searchPageClicks(-1))
    searchPageLeft.pack(side="left")

    searchPageRight = kin.Button(searchButton, text=">", command =lambda: searchPageClicks(1))
    searchPageRight.pack(side="left")

    # Sets the counters for sets and buttons for left and right,
    # inside the search results.
    searchSCounter = kin.Label(searchButton, text=f"Set 1 of {searchSets}")
    searchSCounter.pack(side="left", padx=10)

    searchSetLeft = kin.Button(searchButton, text="<", command =lambda: searchSetClicks(-1))
    searchSetLeft.pack(side="left")

    searchSetRight = kin.Button(searchButton, text=">", command =lambda: searchSetClicks(1))
    searchSetRight.pack(side="left")


    # Creates that table and lists the rows.
    searchTable = t.Treeview(searchAll, columns=list(range(limiterColumns)),
                                show="headings", height=15)
    searchTable.pack()

    # This allows the table to clear and update for the selected
    # rows and columns.
    def refreshSearch():
        # Column Positioning
        firColumn = searchSet * limiterColumns
        lastColumn = firColumn + limiterColumns
        displayHeaders = colHeaders[firColumn:lastColumn]

        # Starts at 0 for headings
        startAt = 0
        for theHeadings in displayHeaders:
            searchTable.heading(startAt, text=theHeadings, command= lambda c=firColumn + startAt: sortedSearch(c))
            searchTable.column(startAt, width=100, minwidth=60)
            startAt = startAt + 1

        # Row clear
        for varDisplay in searchTable.get_children():
            searchTable.delete(varDisplay)

        firRow = searchPage * limiterRows
        lastRow = firRow + limiterRows

        for oRows in obtainRows[firRow:lastRow]:
            searchTable.insert("", "end", values=oRows[firColumn:lastColumn])

    def sortedSearch(column):
        sort.sortedCols(obtainRows, column, sortedDirection)
        refreshSearch()
    refreshSearch()