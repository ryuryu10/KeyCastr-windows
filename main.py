from pynput.keyboard import Key, Listener
from module import window

def func(key):
    print(key)




if __name__ == "__main__":
    with Listener(on_press=func) as listener:
        window.Window_design()
        window.root.mainloop()
        listener.join()
    
