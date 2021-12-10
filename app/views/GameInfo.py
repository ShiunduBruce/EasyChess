import tkinter as tk


class GameInfo:
    def __init__(self) -> None:
        self.fields = 'First Name', 'Second Name'

    def fetch(self, entries):
        for entry in entries:
            field = entry[0]
            text = entry[1].get()
            print('%s: "%s"' % (field, text)) 

    def makeform(self, root, fields):
        entries = []
        for field in fields:
            row = tk.Frame(root)
            lab = tk.Label(row, width=15, text=field, anchor='w')
            ent = tk.Entry(row)
            row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
            lab.pack(side=tk.LEFT)
            ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
            entries.append((field, ent))
        return entries

    def diplay(self):
        root = tk.Tk()
        ents = self.makeform(root, self.fields)
        root.bind('<Return>', (lambda event, e=ents: self.fetch(e)))   
        b1 = tk.Button(root, text='Enter',
                    command=(lambda e=ents: self.fetch(e)))
        b1.pack(side=tk.LEFT, padx=5, pady=5)
        b2 = tk.Button(root, text='Enter', command=root.quit)
        b2.pack(side=tk.LEFT, padx=5, pady=5)
        root.mainloop()
