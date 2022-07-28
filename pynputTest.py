from pynput import keyboard
import sys

def on_release(key):
    if key == keyboard.Key.up:
        semaphore = 1
        print('changed')

# Collect events until released
with keyboard.Listener(
        on_release=on_release) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_release=on_release)
listener.start()




