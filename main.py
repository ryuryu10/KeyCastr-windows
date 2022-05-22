from pynput.keyboard import Key, Listener
from module import window, keyboard

if __name__ == "__main__":
    with Listener(on_press=keyboard.func) as listener:
        window.win.mainloop()
        listener.join()
