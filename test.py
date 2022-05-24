from tkinter import Label, Tk, Canvas, BOTH, PhotoImage, Toplevel
from tkinter.constants import BOTTOM, E, NW, RAISED, TOP

root = Tk()
root.overrideredirect(1)
root.attributes("-transparentcolor", 'white')
root.attributes("-topmost", 1)
root.geometry("500x500")

# Creating a canvas for placing the squircle shape.
canvas = Canvas(root, height=500, width=500, highlightthickness=0, bg='white')
canvas.pack(fill=BOTH, expand=1)

def place_center(): # Placing the window in the center of the screen
    global x, y
    rx = root.winfo_screenwidth()
    ry = root.winfo_screenheight()
    x = int((rx/2) - (500/2))
    y = int((ry/2) - (500/2))
    root.geometry(f"500x500+{x}+{y}")

def move(event):
        global rect
        fx = root.winfo_pointerx() - 250
        fy = root.winfo_pointery() - 10
        try:
                root.geometry(f"{x}x{ht}+{fx}+{fy}")
        except Exception:
                root.geometry(f"500x500+{fx}+{fy}")
        # if fx > 1 and fy > 1:
        #         canvas.delete(rect)
        #         rect = round_rectangle(0, 0, fx, fy, radius=50, fill="#1fa5fe")


def round_rectangle(x1, y1, x2, y2, radius=25, **kwargs): # Creating a rounded rectangle
        
        points = [x1+radius, y1,
                x1+radius, y1,
                x2-radius, y1,
                x2-radius, y1,
                x2, y1,
                x2, y1+radius,
                x2, y1+radius,
                x2, y2-radius,
                x2, y2-radius,
                x2, y2,
                x2-radius, y2,
                x2-radius, y2,
                x1+radius, y2,
                x1+radius, y2,
                x1, y2,
                x1, y2-radius,
                x1, y2-radius,
                x1, y1+radius,
                x1, y1+radius,
                x1, y1]

        return canvas.create_polygon(points, **kwargs, smooth=True)
def cl(event):
        root.quit()
        
def resize(event):
        global rect
        global x, y, ht
        x = root.winfo_pointerx() - root.winfo_rootx()
        y = root.winfo_pointery() - root.winfo_rooty()
        if x > 0:
                fx = root.winfo_rootx()
                fy = root.winfo_rooty() + y
                ht = root.winfo_height() - y
                if ht > 0:
                        root.geometry(f"{x}x{ht}+{fx}+{fy}")
                        canvas.delete(rect)
                        rect = round_rectangle(0, 0, x, ht, radius=50, fill="#1fa5fe")

place_center()

top = Canvas(canvas, height=50, bg="#1fa5fe", highlightthickness=0)
top.pack(side=TOP, pady=2)

# Creating the squircle
rect = round_rectangle(0, 0, 500, 500, radius=50, fill="#1fa5fe")


root.bind("<Button-3>", cl)

rx = root.winfo_rootx()
ry = root.winfo_rooty()
root.unbind("<B1-Motion>")

root.mainloop()