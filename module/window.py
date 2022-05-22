import tkinter as tk
import tkinter.ttk as ttk
import tkinter.scrolledtext as tkst

root = tk.Tk()

def Window_design():
    Frame1 = ttk.Frame(root)
    Frame1.place(relx=0.01, rely=0.013, relheight=0.975,relwidth=0.375)
    Frame1.configure(relief='groove')
    Frame1.configure(relief='groove')
    Frame1.configure(borderwidth="2")
    Frame1.configure(cursor="fleur")