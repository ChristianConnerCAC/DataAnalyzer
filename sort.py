# User Story Sort
# Selected columns get sorted
def sortedCols(rowStarters, column, sortedDirection):

    # Allows for ascending and descending for sorting.
    if sortedDirection.get(column, False) == False:
        sortedDirection[column] = True
    else:
        sortedDirection[column] = False

    # This helps check the values in the selected.
    # Does multiple checks for:
    # if row has the column
    # if the value is a whole number
    # if the value is a decimal
    # if the value is a negative number
    # then sorts the value as text
    def sortedValues(row):
        if column >= len(row):
            value = ""
        else:
            value = str(row[column])
        if value.isdigit():
            return(0, float(value))
        elif value.replace(".", "", 1).isdigit():
            return(0, float(value))
        elif value.replace("-","", 1).replace(".","",1).isdigit():
            return(0, float(value))
        else:
            return(1, value.lower())

    # This is for srting the rows using the selected
    # Or revereses the rows for descending.
    rowStarters.sort(key = sortedValues)
    if sortedDirection[column] == False:
        rowStarters.reverse()