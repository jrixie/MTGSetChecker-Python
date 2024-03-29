from tkinter import *

from ScrollCanvas import ScrollCanvas
from tkinter.scrolledtext import ScrolledText

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
        self.sets = Set.all()
        self.sets.sort(key=lambda set: set.release_date, reverse=True)

        setNames = list(set.name for set in self.sets)

        # Create Scroll Canvas
        self.setCheck = ScrollCanvas(root, setNames)

        # Test button for Check Button variable
        self.ok = Button(root, text="OK", command=self.printVar)

        # Add Clear Button
        self.clear = Button(root, text="Uncheck", command=self.uncheck)

        # Create Entry for Search
        # Create StringVar and bind to callback function on change
        sv = StringVar()
        sv.trace("w", lambda name, index, mode, sv=sv: self.update(sv))
        self.search = Entry(root, textvariable = sv)

        # Create ScrolledText for Cards
        cardsVar = StringVar()
        self.cards = ScrolledText(root)

        self.make_grid()


    def printVar(self):
        var = self.setCheck.checkVar()
        print(var)

        self.parseCards()
        print(self.cardList)

        print(self.crossCheck())

    def crossCheck(self):
        cards = self.parseCards()
        sets = self.parseSets()

        matches = []

        for card in cards:
            cardAPI = Card.where(name=card).all()
            if cardAPI is not None:
                for c in cardAPI:
                    for s in sets:
                        print("Comparing " , s , "to" , c.set_name)
                        if s == c.set_name:
                            matches.append([card, c.set_name])

        return matches

    def make_grid(self):
        self.search.grid(row = 0, column = 0, sticky = "nwe")
        self.setCheck.grid(row = 1, column = 0, sticky = "ws")
        self.ok.grid(row = 3, column = 0, sticky = "nse")
        self.clear.grid(row=2, column=0, sticky="nse")
        self.cards.grid(row = 0, column = 2)

    def parseCards(self):
        self.cardList = self.cards.get(1.0, END).splitlines()
        return self.cardList

    def parseSets(self):
        self.setList = self.setCheck.checkVar()
        return self.setList

    def update(self, sv):
        setList = []

        # Retrieve text from searchbar
        text = self.search.get()

        # Find set names containing the substring
        for set in self.sets:
            if set.name.find(text) != -1:
                setList.append(set.name)

        print(setList)

        # Clear the canvas, update its setList, and populate
        self.setCheck.clear()
        self.setCheck.updateVar(setList)

    def uncheck(self):
        self.setCheck.uncheck()

if __name__ == "__main__":
    root = Tk()
    window = InputWindow(root)
    root.mainloop()
