import tkinter as kin

# This allows for a popup for guidance.
# Hides the popup till dragged over.
def naviHover(message, hover):
    hoverPop = kin.Toplevel(hover)
    hoverPop.withdraw()

    # The popup message style from alignment, background and color

    messageGuide = kin.Label(hoverPop, text=message, foreground="white",
                             background="black", relief="solid", justify="left", borderwidth=1)
    messageGuide.pack()

    # Shows popup next to the mouse
    # deiconify displays it.
    def popGuide(hoverOver):
        hoverPop.geometry(f"+{hoverOver.x_root + 10}+{hoverOver.y_root}")
        hoverPop.deiconify()

    # When the mouse leaves it goes away.
    # Enters and Leaves the popup
    def unpopGuide(hoverOver):
        hoverPop.withdraw()

    hover.bind("<Enter>", popGuide)
    hover.bind("<Leave>", unpopGuide)