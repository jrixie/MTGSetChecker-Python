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

        # Create Scroll Canvas
        self.setCheck = ScrollCanvas(root)

        # Test button for Check Button variable
        self.b = Button(root, text="OK", command=self.printVar)
        self.b.grid(row = 0, column = 2) # .pack()

        self.make_grid()
        self.add_sets()

    def printVar(self):
        var = self.setCheck.checkVar()
        print(var)

    def make_grid(self):
        # Define grid
        total_rows = 3
        total_columns = 3

        rows = range(0, total_rows)
        columns = range(0, total_columns)

        for column in columns:
            self.root.columnconfigure(column, weight=1)

        for row in rows:
            self.root.rowconfigure(row, weight=1, uniform=1)


    def add_sets(self):
        # Retrieve from MTGSDK, sort by release date, and pass into ScrollCanvas
        sets = Set.all()
        sets.sort(key=lambda set: set.release_date, reverse=True)

        setNames = list(set.name for set in sets)
        self.setCheck.populate(setNames)


if __name__ == "__main__":
    root = Tk()
    window = InputWindow(root)
    root.mainloop()
