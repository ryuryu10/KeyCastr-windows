from typing import List
from pynput.keyboard import Key, Listener

def func(key):
    print(key)

with Listener(on_press=func) as listener:
    listener.join()