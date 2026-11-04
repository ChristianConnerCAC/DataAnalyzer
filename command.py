# end always puts the line after in this case starts at the beginning.
def helpCommand(infoBox):
    infoBox.insert("end", 'Type "Help" without the " into the command box to get started.\n')
    infoBox.insert("end", 'Command Box: ')

    # User can press Enter and create another command box.
    def enterKey(buttonPress):
        newCommand(infoBox)
        return "break"
    #tkinter registers <Return> as enter
    infoBox.bind("<Return>", enterKey)

# Creates a new command box on a new line
def newCommand(infoBox):
    infoBox.insert("end", "\nCommand Box: ")
    #Follows the last line made.
    infoBox.see("end")
    