import tkinter as tk
import tkinter.ttk as ttk
import tkinter.scrolledtext as tkst
import ctypes
import math


def installation():
    User32 = ctypes.windll.user32
    User_Screen_Middle_width = math.trunc((User32.GetSystemMetrics(0) / 2))
    User_Screen_Middle_height = math.trunc((User32.GetSystemMetrics(1) / 2))
    Program_ScreenSize_width = 400
    Program_ScreenSize_height = 400
    MPSW = math.trunc(Program_ScreenSize_width / 2)
    MPSH = math.trunc(Program_ScreenSize_height / 2)
    Screen_Size = "{0}x{1}+{2}+{3}".format(
        Program_ScreenSize_width,
        Program_ScreenSize_height,
        User_Screen_Middle_width-MPSW,
        User_Screen_Middle_height-MPSH
    )
    return Screen_Size

class Win(tk.Tk):

    def __init__(self,master=None):
        tk.Tk.__init__(self,master)
        self.geometry(installation())
        self.resizable(False, False)
        self.wm_attributes("-topmost", 1)
        self.overrideredirect(True)
        self.lift()
        self._offsetx = 0
        self._offsety = 0
        self.bind('<Button-1>',self.clickwin)
        self.bind('<B1-Motion>',self.dragwin)

    def dragwin(self,event):
        x = self.winfo_pointerx() - self._offsetx
        y = self.winfo_pointery() - self._offsety
        self.geometry('+{x}+{y}'.format(x=x,y=y))

    def clickwin(self,event):
        self._offsetx = event.x
        self._offsety = event.y


win = Win()
