import pandas as pd
import tkinter as tk
import tkinter.filedialog as fd
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
from scipy.stats import norm
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
        df_numeric = df[["raza"]].apply(pd.to_numeric, errors='coerce')
        # df_numeric = df_numeric.dropna()
        edad = df["edad"]
        raza = df_numeric["raza"]
    except Exception as e:
        # display an error message if an exception is caught
        messagebox.showerror("Error", f"Check your column names")
        print(e)
        return

    try:
        # Create a new window to display the first graph
        windowAge = tk.Toplevel(root)
        windowAge.geometry("600x400")
         # Plot the normal distribution of the columns
        figAge = Figure(figsize=(5, 4), dpi=100)
        axAge = figAge.add_subplot(111)
        mean = np.mean(edad)
        std_dev = np.std(edad)
        x = np.linspace(mean - 3*std_dev, mean + 3*std_dev, 100)
        y = 1/(std_dev * np.sqrt(2*np.pi)) * np.exp(-(x-mean)**2/(2*std_dev**2))
     
        axAge.plot(x, y)
        axAge.set_title("Distribución normal de la edad")
        axAge.set_xlabel("Edad")
        axAge.set_ylabel("Frecuencia")

        # Create a canvas for the first plot
        canvasAge = FigureCanvasTkAgg(figAge, master=windowAge)
        canvasAge.draw()
        canvasAge.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        # Create a new window to display the second graph
        windowBreed = tk.Toplevel(root)
        windowBreed.geometry("600x400")
        print(raza)
        print(x)
        print(y)
        print(mean)
        print(std_dev)
        #Plot the normal distribution of the raza column
        figBreed, axBreed = plt.subplots(figsize=(5, 5))
        x = np.linspace(raza.min(), raza.max(), 100)
        y = norm.pdf(x, raza.mean(), raza.std())
        axBreed.plot(x, y, 'b-', lw=2)
        axBreed.set_title("Distribución normal de la raza")
        axBreed.set_xlabel("Raza")
        axBreed.set_ylabel("Frecuencia")
        axBreed.tick_params(labelsize=4)


        #Create a canvas for the second plot
        canvasBreed = FigureCanvasTkAgg(figBreed, master=windowBreed)
        canvasBreed.draw()
        canvasBreed.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        #Add the navigation toolbar to the plot window
        toolbar = NavigationToolbar2Tk(canvasBreed, windowBreed)
        toolbar.update()
    except Exception as e:
        # display an error message if an exception is caught
        messagebox.showerror("Error", f"Check your column data")
        print(e)
        return
   

root = tk.Tk()
root.geometry("1200x800")
root.title("Gaussian Bell")
# Add a button to select an Excel file
button = tk.Button(root, text='Select File', command=browse_file)
button.pack(side=tk.TOP, pady=10)

try:
    root.mainloop()
except Exception as e:
    # display an error message if an exception is caught
    messagebox.showerror("Error", "Something happend, check logs")
    print(e)