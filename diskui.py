from tkinter import *  
from tkinter import ttk

def calculateur(): 
    root2 = Tk()
    try:
        # Fetching values from the entries and converting them to float for calculations
        a = float(labelTitle.get())
        b = float(labelTitle2.get())
        total = b / a
        ttk.Label(root2, text=f"Disk utilisé a : {total*100} %").grid(row=1, column=0)
    except ValueError:
        # Handling cases where non-numeric values are entered
        ttk.Label(root2, text="Veuillez entrer des valeurs numériques valides").grid(row=1, column=0)
    root2.mainloop()

root = Tk()

# Correcting label variable names and grid placement
labelTitle1 = ttk.Label(root, text="Total Capacity (Gb)")
labelTitle = ttk.Entry(root)

labelTitle20 = ttk.Label(root, text="Used Capacity (Gb)")
labelTitle2 = ttk.Entry(root)

button = ttk.Button(root, text="persent usage", command=calculateur)

# Placing widgets on the grid
labelTitle1.grid(row=1, column=0)
labelTitle.grid(row=1, column=1)

labelTitle20.grid(row=2, column=0)
labelTitle2.grid(row=2, column=1)

button.grid(row=3, column=1)

root.mainloop()
