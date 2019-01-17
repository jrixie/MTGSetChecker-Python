import tkinter as tk

class ScrollCanvas(tk.Frame):
    def __init__(self, root):

        tk.Frame.__init__(self, root)
        self.canvas = tk.Canvas(root, borderwidth=0, background="#ffffff")
        self.frame = tk.Frame(self.canvas, background="#ffffff")
        self.vsb = tk.Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)

        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((4,4), window=self.frame, anchor="nw",
                                  tags="self.frame")

        self.frame.bind("<Configure>", self.onFrameConfigure)

    def populate(self, data):
        self.selected = {}
        self.setList = data;
        for idx, point in enumerate(self.setList):
            self.selected[idx] = tk.IntVar()
            tk.Checkbutton(self.frame, text=point, variable=self.selected[idx]).grid(row=idx, column=0, sticky='w')

    def checkVar(self):
        sets = []
        for idx, var in enumerate(self.setList):
            if self.selected[idx].get() == 1:
                sets.append(var)

        return sets

    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
