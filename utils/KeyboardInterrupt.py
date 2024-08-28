from pynput import keyboard


class KeyboardInterrupt:

    @staticmethod
    def on_press(key):
        try:
            print('alphanumeric key {0} pressed'.format(key.char))
        except AttributeError:
            print('special key {0} pressed'.format(key))

    @staticmethod
    def on_release(key):
        print('{0} released'.format(key))
        if key == keyboard.Key.esc:
            # Stop listener
            return False

    @staticmethod
    def start():
        listener = keyboard.Listener(
            on_press=KeyboardInterrupt.on_press,
            on_release=KeyboardInterrupt.on_release)
        listener.start()

    # FIXME pulir
