import copy as c

# end always puts the line after in this case starts at the beginning.
def helpCommand(infoBox, tableStored, entryUpdate, closeTable, calcFunc2):
    infoBox.insert("end", 'Type "Help" without the " into the command box to get started.\n')
    infoBox.insert("end", f"Table Loaded in {calcFunc2:.6f} seconds\n")
    infoBox.insert("end", 'Command Box: ')
    infoBox.mark_set("input_start", "end-1c")
    infoBox.mark_gravity("input_start", "left")
    entryPass = [False]
    undoHistory = []
    redoHistory = []

    def backspaceKey(buttonPress):
        if infoBox.compare("insert", "<=", "input_start"):
            return "break"

    # User can press Enter and create another command box.
    def enterKey(buttonPress):

        # Finds the command entered at current line
        # Replaces those instructions
        # Adds the new information and refreshes table
        # Then checks if they want to add a row or columy with entry
        # "end-1c linestart" = Tkinter Beginning of the current line
        # "end-1c" = end of the text
        findCommand = infoBox.get("end-1c linestart", "end-1c")
        findCommand = findCommand.replace("Command Box: ", "", 1)

        if entryPass[0] == True:
            findCommand = findCommand.replace("Add a row or column: ", "")

            if findCommand.lower() == "end":
                entryPass[0] = False
                infoBox.insert("end", "\nEntry stopped: Type other commands or Help.")

            elif entry(tableStored, findCommand):
                undoHistory.append(c.deepcopy(tableStored))
                redoHistory.clear()
                entryUpdate()
                entryPass[0] = False
                infoBox.insert("end", "\nEntry added.")
                # Mark set and Mark Gravity
            else:
                infoBox.insert("end", "\nIncorrect Entry.")
                infoBox.insert("end", "\nPlease try again or type End to stop the command.")
                infoBox.insert("end", "\n Add a row or column: ")
                infoBox.mark_set("input_start", "end-1c")
                infoBox.mark_gravity("input_start", "left")
                return "break"
        # This allows the usage of Undo in the command bar
        # Gives back their last entry
        elif findCommand.lower() == "undo":
            if undoHistory:
                # It will save the current so the user can redo it later if needed.
                # Then resotres the previous version of the table.
                redoHistory.append(c.deepcopy(tableStored))
                tableStored[:] = undoHistory.pop()
                # Updates the table for the changes.
                entryUpdate()
                infoBox.insert("end", "\n Undone last entry.")
            else:
                infoBox.insert("end", "\n Undid nothing.")
        # This allows usage of  Redo in the command bar
        # Puts back what was taken away.
        elif findCommand.lower() == "redo":
            if redoHistory:
                # Saves the current table if user wants to undo it again.
                # Restores the entry if undid.
                undoHistory.append(c.deepcopy(tableStored))
                tableStored[:] = redoHistory.pop()
                # Updates the table.
                entryUpdate()
                infoBox.insert("end", "\n Restored Entry.")
            else:
                infoBox.insert("end", "\n Nothing to Restore.")
        
        # Closes the program back to main screen.
        elif findCommand.lower() == "close":
            closeTable()
            return "break"

        # Commentary on what help does
        # When the user types help      
        elif findCommand.lower() == "help":
            infoBox.insert("end", "\n Type Help as the prefix then what you need help on in the list below.")
            infoBox.insert("end", "\n For Example: Help Entry")
            infoBox.insert("end", "\nAvailable Commands:")
            infoBox.insert("end", "\nUndo - Undoes the previous command")
            infoBox.insert("end", "\nRedo = Restores the command.")
            infoBox.insert("end", "\nClose = Closes the table and returns to main screen.")
            infoBox.insert("end", "\nEntry - Manually adds a row or column to your table.")

        # Commentary on what help entry does
        # When the user types help entry.
        elif findCommand.lower() == "help entry":
            infoBox.insert("end", "\n Entry allows you to add a row or column to your table.")
            infoBox.insert("end", "\n Use R (for Row) followed by a row number shown on the table to add a row.")
            infoBox.insert("end", "\n Use C (for Column) followed by a row number shown on the table to add a Column.")
            infoBox.insert("end", "\n After the number follow it with a '+' or '-' to go after or before the row / column.")
            infoBox.insert("end", "\n For Example: R1+ = Add this Row After Row 1 on the table making your add on Row 2.")
            infoBox.insert("end", "\n While R1- = Add this row Before Row 1. Making your new one in R1 and moving the old R1 forward")
            infoBox.insert("end", "\n When you manually place in press Tab for each new piece of data")
            infoBox.insert("end", "\n Example: R1+ [Tab] 1 [Tab] 2 [Tab] 3 [Tab] 4 (Tab is your seperator.)")

        # Commentary for entry
        elif findCommand.replace("Command Box: ", "").lower() == "entry":
            infoBox.insert("end", "\nAdd a row or column: ")
            infoBox.mark_set("input_start","end-1c")
            infoBox.mark_gravity("input_start", "left")

            entryPass[0] = True
            return "break"

        # Error handling for other than what we have in commands.
        else:
            infoBox.insert("end",f"\n Incorrect Input Command: {findCommand}")
            infoBox.insert("end","\n Please try again. Type Help to see available commands.")
        newCommand(infoBox)
        return "break"


    # TabKey allows for the separation
    def tabKey(buttonPress):
        infoBox.insert("insert", "\t")
        return "break"

    #tkinter registers <Return> as Enter
    #tkinter registers <Tab> as Tab
    infoBox.bind("<Return>", enterKey)
    infoBox.bind("<Tab>", tabKey)
    infoBox.bind("<BackSpace>", backspaceKey)

# Creates a new command box on a new line
def newCommand(infoBox):#
    infoBox.insert("end", "\nCommand Box: ")
    infoBox.mark_set("input_start", "end-1c")
    infoBox.mark_gravity("input_start", "left")
    #Follows the last line made.
    infoBox.see("end")
    infoBox.yview("scroll", -infoBox.winfo_height(), "pixels")

# This allows for a new row or column to the table
# By separating the information using tab
# Or checks if the user wants to add a column.

def entry(tableStored, findCommand):
    # Separates the command from the data entered by user
    # Then gets a position number from the command
    findData = findCommand.split("\t")
    rcCommand = findData[0]
    # Then checks the command if their is enough information
    if len(rcCommand) < 3:
        return False
    # Checks a user is adding a row or column
    if rcCommand[0].upper() != "R":
        if rcCommand[0].upper() != "C":
            return False
    # Checks before or after 
    if rcCommand[-1] != "+":
        if rcCommand[-1] != "-":
            return False
    # Checks position is a number
    if rcCommand[1:-1].isdigit() == False:
        return False
    # Then checks if the user wants to add a row
    rcPosition = int(rcCommand[1:-1])

    if rcCommand[0].upper() == "R":
        if rcCommand[-1] == "-":
            rowPosition = rcPosition - 1
        else:
            rowPosition = rcPosition
        tableStored.insert(rowPosition + 1, findData[1:])
    elif rcCommand[0].upper() == "C":
        if rcCommand[-1] == "-":
            columnPosition = rcPosition - 1
        else:
            columnPosition = rcPosition
        # Adds the new column to the row.
        for fixedPlace in range(len(tableStored)):
            if fixedPlace + 1 < len(findData):
                tableStored[fixedPlace].insert(columnPosition, findData[fixedPlace + 1])
            else:
                # Cell is left empty if no value.
                tableStored[fixedPlace].insert(columnPosition, "")
    return True