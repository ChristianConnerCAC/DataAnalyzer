import tkinter as kin

# Displays the third screen called "Graph View"
# Geometry matches with DA.py
def graphView(display, rowStarters, colHeaders):
    graphDisplay = kin.Toplevel(display)
    graphDisplay.title("Graph View")
    graphDisplay.geometry("2000x1000")

    # Canvas for the Graph
    graphCanvas = kin.Canvas(graphDisplay, width=900, height=500)
    graphCanvas.pack(pady=30)

    # Creates the Row Section
    rowSection = kin.Frame(graphDisplay)
    rowSection.pack(side="top", anchor="center", pady=5)

    rowLines = kin.Frame(rowSection)
    rowLines.pack(side="top")
    # Section for setting the X values
    xAxisSection = kin.Frame(graphDisplay)
    xAxisSection.pack(side="bottom", anchor="w", padx=20, pady=5)

    # X Value Entry
    intervalLabel = kin.Label(xAxisSection, text="(X-Axis) Intervals of:", font=("Courier New", 12))
    intervalLabel.pack(side="left", padx=5)

    intervalEntry = kin.Entry(xAxisSection, width=8, font=("Courier New", 12))
    intervalEntry.pack(side="left", padx=5)

    # Enter the number for X-Axis Segments
    segmentLabel = kin.Label(xAxisSection, text="(X-Axis) Segments:", font=("Courier New", 12))
    segmentLabel.pack(side="left", padx=5)

    segmentEntry = kin.Entry(xAxisSection, width=8, font=("Courier New", 12))
    segmentEntry.pack(side="left", padx=5)

    # Repeats for Y-Axis values, entry, and segments.
    yAxisSection = kin.Frame(graphDisplay)
    yAxisSection.pack(side="bottom", anchor="w", padx=20, pady=5)

    yIntervalLabel = kin.Label(yAxisSection, text="(Y-Axis) Intervals of:", font=("Courier New", 12))
    yIntervalLabel.pack(side="left", padx=5)

    yIntervalEntry = kin.Entry(yAxisSection, width=8, font=("Courier New", 12))
    yIntervalEntry.pack(side="left", padx=5)

    ySegmentLabel = kin.Label(yAxisSection, text="(Y-Axis) Segments:", font=("Courier New", 12))
    ySegmentLabel.pack(side="left", padx=5)

    ySegmentEntry = kin.Entry(yAxisSection, width=8, font=("Courier New", 12))
    ySegmentEntry.pack(side="left", padx=5)

    # Updates the ticks for X-aXIS
    def updateXAxis():
        graphCanvas.delete("xLabels")

        try:
            interval = int(intervalEntry.get())
            segments = int(segmentEntry.get())

            # Checks for positive
            # Then creates the marks.
            if interval <= 0:
                return

            if segments <= 0:
                return

            for x in range(1, segments + 1):
                xPosition = 100 + (750 / segments) * x
                xValue = interval * x

                graphCanvas.create_text(xPosition, 465, text=str(xValue), tags="xLabels", font=("Courier New", 10))
                graphCanvas.create_line(xPosition, 450, xPosition, 440, tags="xLabels", width=2)
        except ValueError:
            return

    # Repeats from the X-Axis but this time for the Y-axis
    def updateYAxis():
        graphCanvas.delete("yLabels")

        try:
            interval = int(yIntervalEntry.get())
            segments = int(ySegmentEntry.get())

            if interval <= 0:
                return

            if segments <= 0:
                return

            for y in range(1, segments + 1):
                yPosition = 450 - (400 / segments) * y
                yValue = interval * y

                graphCanvas.create_text(80, yPosition, text=str(yValue), tags="yLabels", font=("Courier New", 10))
                graphCanvas.create_line(100, yPosition, 110, yPosition, tags="yLabels", width=2)
        except ValueError:
            return

    #First row section and position in the first column.
    firstRow = kin.Frame(rowLines)
    firstRow.grid(row=0, column=0, padx=10,pady=3, sticky="W")
     
    # Creates the row selection labels.
    rowLabel = kin.Entry(firstRow, width=12, font=("Courier New", 14))
    rowLabel.insert(0, "Line 1:")
    rowLabel.pack(side="left", padx=5)

    def saveName(selected):
        rowLabel.master.focus_set()
    rowLabel.bind("<Return>", saveName)

    # Draws the selected row as a line graph.
    # Removes the previous graph line
    # Gets from the dropdown
    def updateGraph():
        graphCanvas.delete("graphLine")

        for rowIndex in range(len(rowSelections)):
            selectedRow = rowSelections[rowIndex].get()

            if selectedRow == "Select Row":
                continue

            rowValues = rowStarters[int(selectedRow) - 1]
            points = []

            # Calculates the canvas position for each row value.
            for x in range(len(rowValues)):
                xPosition = 100 + (750 / (len(rowValues) - 1)) * x
                yPosition = 450 - (int(rowValues[x]) * 400/ 1000)

                points.append((xPosition, yPosition))

            for x in range(len(points) - 1):
                graphCanvas.create_line(points[x][0], points[x][1], points[x + 1][0], points[x + 1][1], fill="blue", width=2, tags="graphLine")

    rowSelections = []

    # Creates the dropdown menu for selecting a row.
    rowOptions = kin.StringVar()
    rowOptions.set("Select Row")

    rowSelections.append(rowOptions)

    rowMenu = kin.OptionMenu(firstRow, rowOptions, *range(1, len(rowStarters) +1), command=lambda selected: updateGraph())
    rowMenu.pack(side="left", padx=5)

    # Keep track of a limited amount of rows to be added
    rowCount = [1]


    # Adds another row selection from dropdown when the user clicks "+"
    def addRow():
        if rowCount[0] < 10:
            newRow = kin.StringVar()
            newRow.set("Select Row")

            rowSelections.append(newRow)

            column = (rowCount[0]) // 5
            row = (rowCount[0]) % 5

            newLine = kin.Frame(rowLines)
            newLine.grid(row=row, column=column, padx=10, pady=3, sticky="w")

            newLabel = kin.Entry(newLine, width=12, font=("Courier New", 14))
            newLabel.insert(0, "Line " + str(rowCount[0] + 1) + ":")
            newLabel.pack(side="left", padx=5)

            newLabel.bind("<Return>", lambda selected: newLine.focus_set())

            newMenu = kin.OptionMenu(newLine, newRow, *range(1, len(rowStarters) + 1), command=lambda selected: updateGraph())
            newMenu.pack(side="left",padx=5)

            rowCount[0] = rowCount[0] + 1

    # These are buttons to activate:
    # Row Dropdown
    # Update X Axis
    # Update Y Axis
    addButton = kin.Button(rowSection, text="+", command=addRow, font=("Courier New", 14))
    addButton.pack(side="left", padx=5)

    updateButton = kin.Button(xAxisSection, text="Update X-Axis", command=updateXAxis)
    updateButton.pack(side="left", padx=5)

    yUpdateButton = kin.Button(yAxisSection, text="Update Y-Axis", command=updateYAxis)
    yUpdateButton.pack(side="left", padx=5)

    # Currently draws the lines for x-axis and y-axis
    graphCanvas.create_line(100,450,850,450,width=2)
    graphCanvas.create_line(100,450,100,50,width=2)
