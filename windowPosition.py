import tkinter as kin

def createGrid(display, window):
    positionGrid = kin.Frame(display)

    leftButton=  kin.Button(positionGrid, text="TL", width=4, height=2, command=lambda: screenPosition(window,"topLeft"))
    leftButton.grid(row=0, column=0)

    topButton = kin.Button(positionGrid, text="T", width=4, height=2, command=lambda: screenPosition(window,"top"))
    topButton.grid(row=0, column=1)

    rightButton = kin.Button(positionGrid, text="TR", width=4, height=2, command=lambda: screenPosition(window,"topRight"))
    rightButton.grid(row=0, column=2)

    middleLeft = kin.Button(positionGrid, text="ML", width=4, height=2, command=lambda: screenPosition(window,"left"))
    middleLeft.grid(row=1, column=0)

    centerButton = kin.Button(positionGrid, text="C", width=4, height=2, command=lambda: screenPosition(window,"center"))
    centerButton.grid(row=1,column=1)

    middleRight = kin.Button(positionGrid, text="MR", width=4, height=2, command=lambda: screenPosition(window,"right"))
    middleRight.grid(row=1, column=2)

    bottomLeft = kin.Button(positionGrid, text="BL", width=4, height=2, command=lambda:  screenPosition(window,"bottomLeft"))
    bottomLeft.grid(row=2,column=0)

    bottomButton = kin.Button(positionGrid, text="B", width=4, height=2, command=lambda:  screenPosition(window,"bottom"))
    bottomButton.grid(row=2, column=1)

    bottomRight = kin.Button(positionGrid, text="BR", width=4, height=2, command=lambda:  screenPosition(window,"bottomRight"))
    bottomRight.grid(row=2, column=2)

    return positionGrid

def screenPosition(window, position):
    screenWidth = window.winfo_screenwidth()
    screenHeight = window.winfo_screenheight() - 70

    windowWidth = window.winfo_width()
    windowHeight = window.winfo_height()

    if position =="left":
        window.geometry(f"+0+{(screenHeight - windowHeight) // 2}")
    if position =="right":
        window.geometry(f"+{screenWidth - windowWidth}+{(screenHeight - windowHeight) // 2}")
    if position =="top":
        window.geometry(f"+{(screenWidth - windowWidth) // 2}+0")
    if position =="bottom":
        window.geometry(f"+{(screenWidth - windowWidth) // 2}+{screenHeight - windowHeight}")
    if position == "topLeft":
        window.geometry("+0+0")
    if position == "topRight":
        window.geometry(f"+{screenWidth - windowWidth}+0")
    if position == "bottomLeft":
        window.geometry(f"+0+{screenHeight - windowHeight}")
    if position == "bottomRight":
        window.geometry(f"+{screenWidth - windowWidth}+{screenHeight - windowHeight}")
    if position == "center":
        window.geometry(f"+{(screenWidth - windowWidth) // 2}+{(screenHeight - windowHeight) // 2}")
        