from pynput import keyboard
import os


class KeyboardInterrupter:

    def __init__(self, action_on_close):
        self.action_on_close = action_on_close

    def start(self):
        listener = keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_release)
        listener.start()

    def on_press(self, key):
        pass

    def on_release(self, key):
        if key == keyboard.Key.esc:
            self.action_on_close()
            os._exit(0)
            # Stop listener
            return False
