import pandas as pd
import tkinter as tk
import tkinter.filedialog as fd
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
import scipy.stats as stats

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
        windowAge.geometry("600x400")
         # Plot the normal distribution of the columns
        fig1, axAge = plt.subplots(figsize=(5, 5))
        x = np.linspace(edad.min(), edad.max(), 100)
        y = norm.pdf(x, edad.mean(), edad.std())
        axAge.plot(x, y, 'r-', lw=2)
        axAge.set_title("Distribución normal de la edad")
        axAge.set_xlabel("Edad")
        axAge.set_ylabel("Frecuencia")

        # Create a canvas for the first plot
        canvasAge = FigureCanvasTkAgg(fig1, master=windowAge)
        canvasAge.draw()
        canvasAge.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        # Create a new window to display the second graph
        windowBreed = tk.Toplevel(root)
        windowBreed.geometry("600x400")
        
        # Plot the normal distribution of the raza column
        figBreed, axBreed = plt.subplots(figsize=(5, 5))
        x = np.linspace(raza.min(), raza.max(), 100)
        y = norm.pdf(x, raza.mean(), raza.std())
        axBreed.plot(x, y, 'b-', lw=2)
        axBreed.set_title("Distribución normal de la raza")
        axBreed.set_xlabel("Raza")
        axBreed.set_ylabel("Frecuencia")
        axBreed.tick_params(labelsize=4)


        # Create a canvas for the second plot
        canvas2 = FigureCanvasTkAgg(figBreed, master=windowBreed)
        canvas2.draw()
        canvas2.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        # Add the navigation toolbar to the plot window
        toolbar = NavigationToolbar2Tk(canvas2, windowBreed)
        toolbar.update()
    except Exception as e:
        # display an error message if an exception is caught
        messagebox.showerror("Error", f"Check your column data")
        print(e)
        return
   

root = tk.Tk()
root.geometry("1200x800")

# Add a button to select an Excel file
button = tk.Button(root, text='Select File', command=browse_file)
button.pack(side=tk.TOP, pady=10)

try:
    root.mainloop()
except Exception as e:
    # display an error message if an exception is caught
    messagebox.showerror("Error", "Something happend, check logs")
    print(e)