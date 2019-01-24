from tkinter import *

from ScrollCanvas import ScrollCanvas

from mtgsdk import Card
from mtgsdk import Set


class InputWindow:
    def __init__(self, root):
        self.root = root
        root.title("MTG Set Checker")

        # Define screen size based on user's screen
        screen_width = int(root.winfo_screenwidth() / 2)
        screen_height = int(root.winfo_screenheight() / 2)

        self.width = screen_width
        self.height = screen_height

        window_geometry = str(self.width) + 'x' + str(self.height)
        self.root.geometry(window_geometry)

        # Retrieve from MTGSDK, sort by release date, and pass into ScrollCanvas
        sets = Set.all()
        sets.sort(key=lambda set: set.release_date, reverse=True)

        setNames = list(set.name for set in sets)

        # Create Scroll Canvas
        self.setCheck = ScrollCanvas(root, setNames)

        # Test button for Check Button variable
        self.b = Button(root, text="OK", command=self.printVar)


        self.make_grid()

    def printVar(self):
        var = self.setCheck.checkVar()
        print(var)

    def make_grid(self):
        self.setCheck.grid(row = 0, column = 0, sticky = "nws")
        self.b.grid(row = 0, column = 2)  # .pack()

        # for column in columns:
        #     self.root.columnconfigure(column, weight=1)
        #
        # for row in rows:
        #     self.root.rowconfigure(row, weight=1, uniform=1)



if __name__ == "__main__":
    root = Tk()
    window = InputWindow(root)
    root.mainloop()
