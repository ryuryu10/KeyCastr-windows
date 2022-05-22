import tkinter as tk
import tkinter.ttk as ttk
import tkinter.scrolledtext as tkst
import ctypes
import math

root = tk.Tk()

def installation():
    User32 = ctypes.windll.user32
    User_Screen_Middle_width = math.trunc((User32.GetSystemMetrics(0) / 2))
    User_Screen_Middle_height = math.trunc((User32.GetSystemMetrics(1) / 2))
    Program_ScreenSize_width = 1000
    Program_ScreenSize_height = 800
    MPSW = math.trunc(Program_ScreenSize_width / 2)
    MPSH = math.trunc(Program_ScreenSize_height / 2)
    Screen_Size = "{0}x{1}+{2}+{3}".format(
        Program_ScreenSize_width,
        Program_ScreenSize_height,
        User_Screen_Middle_width-MPSW,
        User_Screen_Middle_height-MPSH
    )
    root.geometry(Screen_Size)
    root.resizable(False, False)
    root.wm_attributes("-topmost", 1)
    root.overrideredirect(True)
    root.lift()


def design():
    Frame1 = ttk.Frame(root)
    Frame1.place(relx=0.01, rely=0.013, relheight=0.975,relwidth=0.375)
    Frame1.configure(relief='groove')
    Frame1.configure(relief='groove')
    Frame1.configure(borderwidth="2")
    Frame1.configure(cursor="fleur")