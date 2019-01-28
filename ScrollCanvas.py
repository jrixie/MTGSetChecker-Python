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
        self.setList = data;
        self.checkButtons = [];
        self.populate()

        # Bind functions to allow for scrolling only in frame
        self.frame.bind("<Configure>", self.onFrameConfigure)
        self.canvas.bind('<Enter>', self.boundToMousewheel)
        self.canvas.bind('<Leave>', self.unboundToMousewheel)


    def populate(self):
        if len(self.checkButtons) == 0:
            # Iterate through with point and num to add CheckButton to grid location and intvar based on num
            for idx, point in enumerate(self.setList):
                var = tk.IntVar()
                check = tk.Checkbutton(self.frame, text=point, variable=var)
                check.grid(row=idx, column=0, sticky='w')

                self.checkButtons.append((check, var))

        elif len(self.setList) != 0:
            # If a list of checkButtons already exists, use those to maintain IntVar states
            count = 0
            for check, var in self.checkButtons:
                if self.setList[count] == check.cget("text"):
                    check.grid(row=count, column=0, sticky='w')
                    count += 1

                    if count >= len(self.setList):
                        return

            # If the setList is 0, do nothing


    def checkVar(self):
        # Iterate through IntVars and append the name of the sets that are checked
        sets = []
        for check, var in self.checkButtons:
            if var.get():
                sets.append(check.cget("text"))

        return sets


    def updateVar(self, data):
        # Set new data and populate
        self.setList = data
        self.populate()


    def clear(self):
        # Iterate through grid slaves in frame and forget them
        for check in self.frame.grid_slaves():
            check.grid_forget()


    def onFrameConfigure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def onMousewheel(self, event):
        self.canvas.yview_scroll(-1 * int(event.delta / 20), "units")

    def boundToMousewheel(self, event):
        self.canvas.bind_all("<MouseWheel>", self.onMousewheel)

    def unboundToMousewheel(self, event):
        self.canvas.unbind_all("<MouseWheel>")