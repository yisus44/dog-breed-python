import pandas as pd
import tkinter as tk
import tkinter.filedialog as fd
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
import numpy as np
from matplotlib.figure import Figure

def browse_file():
    filetypes = (
        ('Excel files', '*.xlsx'),
    )

    filepath = fd.askopenfilename(
        title='Open a file',
        initialdir='/home/jesus/Downloads',
        filetypes=filetypes)

    if not filepath:
        return

    display_excel_file(filepath)

def display_excel_file(filepath):
    # Read the Excel file using pandas
    df = pd.read_excel(filepath)
    # Get the columns "edad" and "raza"
    try:
        # df_numeric = df[["raza"]].apply(pd.to_numeric, errors='coerce')
        # df_numeric = df_numeric.dropna()
        edad = df["edad"]
        raza = df["raza"]
    except Exception as e:
        # display an error message if an exception is caught
        messagebox.showerror("Error", f"Check your column names")
        print(e)
        return

    try:
        # Create a new window to display the first graph
        windowAge = tk.Toplevel(root)
        windowAge.geometry("400x400")

        agesFigure = plt.figure(figsize=(5, 8), dpi=70)
        axAge = agesFigure.add_subplot(111)
        barAge = FigureCanvasTkAgg(agesFigure, windowAge)
        barAge.get_tk_widget().pack(side=tk.LEFT, fill=tk.NONE)
        agesDataFrame = edad.round(
        decimals=0).value_counts().sort_index()
        agesDataFrame.plot(kind='bar', legend=False, ax=axAge, color="g")
        axAge.set_title('Edad de los canes')
        axAge.set_xlabel("Edad")
        axAge.set_ylabel("Frecuencia")

        windowBreed = tk.Toplevel(root)
        windowBreed.geometry("800x800")
        breedsFigure = plt.figure(figsize=(10, 8), dpi=70)
        axBreed = breedsFigure.add_subplot(111)
        barBreed = FigureCanvasTkAgg(breedsFigure, windowBreed)
        barBreed.get_tk_widget().pack(side=tk.RIGHT, fill=tk.NONE)
        breedsDataFrame = raza.value_counts().sort_index()
        breedsDataFrame.plot(kind='bar', legend=False, ax=axBreed, color="r")
        axBreed.set_title('Raza de los canes')
        toolbar = NavigationToolbar2Tk(barBreed, windowBreed)
        toolbar.update()
    except Exception as e:
        # display an error message if an exception is caught
        messagebox.showerror("Error", f"Check your column data")
        print(e)
        return
   

root = tk.Tk()
root.geometry("1920x1080")
root.title("Info de los canes")
# Add a button to select an Excel file
button = tk.Button(root, text='Select File',width = 100, command=browse_file)
button.pack(side=tk.TOP, pady=10)

try:
    root.mainloop()
except Exception as e:
    # display an error message if an exception is caught
    messagebox.showerror("Error", "Something happend, check logs")
    print(e)