import tkinter as tk

class ScrollCanvas(tk.Frame):
    def __init__(self, root, data):

        tk.Frame.__init__(self, root)
        # Create Canvas Element
        self.canvas = tk.Canvas(root, borderwidth=0) #, background="#ffffff"
        self.frame = tk.Frame(self.canvas) #, background="#ffffff"

        # Create Vertical Scrollbar
        self.vsb = tk.Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)

        self.vsb.grid(row = 0, column = 1, sticky='ns') #.pack(side="right", fill="y")
        self.canvas.grid(row = 0, column = 0) #.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((4,4), window=self.frame, anchor="nw")

        # Save selected for iterating through CheckVar later
        self.selected = {}
        self.setList = data;

        self.populate()

        self.frame.bind("<Configure>", self.onFrameConfigure)
        self.canvas.bind('<Enter>', self.boundToMousewheel)
        self.canvas.bind('<Leave>', self.unboundToMousewheel)

    def populate(self):
        # Iterate through with point and num to add CheckButton to grid location and intvar based on num
        for idx, point in enumerate(self.setList):
            self.selected[idx] = tk.IntVar()
            tk.Checkbutton(self.frame, text=point, variable=self.selected[idx]).grid(row=idx, column=0, sticky='w')

    def checkVar(self):
        # Iterate through IntVars and append the name of the sets that are checked
        sets = []
        for idx, var in enumerate(self.setList):
            if self.selected[idx].get() == 1:
                sets.append(var)

        return sets

    def updateVar(self, data):
        self.setList = data
        self.populate()

    def onFrameConfigure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def onMousewheel(self, event):
        self.canvas.yview_scroll(-1 * int(event.delta / 20), "units")

    def boundToMousewheel(self, event):
        self.canvas.bind_all("<MouseWheel>", self.onMousewheel)

    def unboundToMousewheel(self, event):
        self.canvas.unbind_all("<MouseWheel>")