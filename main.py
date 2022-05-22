from pynput.keyboard import Key, Listener
from module import window, keyboard

if __name__ == "__main__":
    with Listener(on_press=keyboard.func) as listener:
        window.installation()
        window.design()
        window.root.mainloop()
        listener.join()
