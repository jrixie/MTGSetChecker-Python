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
        for idx, point in enumerate(data):
            selected = tk.IntVar()
            tk.Checkbutton(self.frame, text=point.name, variable=selected).grid(row=idx, column=0, padx=2)

            #tk.Label(self.frame, text="%s" % row, width=3, borderwidth="1",
            #        relief="solid").grid(row=row, column=0)
            #t="this is the second column for row %s" %row
            #tk.Label(self.frame, text=t).grid(row=row, column=1)

    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
