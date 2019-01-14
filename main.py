from tkinter import *

from ScrollCanvas import ScrollCanvas

from mtgsdk import Card
from mtgsdk import Set


class InputWindow:
    def __init__(self, root):
        self.root = root
        root.title("MTG Set Checker")

        screen_width = int(root.winfo_screenwidth() / 4)
        screen_height = int(root.winfo_screenheight() / 4)

        self.width = screen_width
        self.height = screen_height

        window_geometry = str(self.width) + 'x' + str(self.height)
        self.root.geometry(window_geometry)

        self.setCheck = ScrollCanvas(root)

        self.make_grid()
        self.add_sets()

    def make_grid(self):
        total_rows = 3
        total_columns = 3

        rows = range(0, total_rows)
        columns = range(0, total_columns)

        for column in columns:
            self.root.columnconfigure(column, weight=1)

        for row in rows:
            self.root.rowconfigure(row, weight=1, uniform=1)


    def add_sets(self):
        # self.listbox = Listbox(selectmode=EXTENDED)
        # self.listbox.grid(row=0, column=0, columnspan=2, sticky=N+S)
        # self.setCheck.grid(row=0, column=0, rowspan=2, sticky=N + S)

        sets = Set.all()
        print(sets)

        self.setCheck.populate(sets)

def main():
    card = Card.find(42)
    print(card.name)


if __name__ == "__main__":
    root = Tk()
    window = InputWindow(root)
    root.mainloop()
