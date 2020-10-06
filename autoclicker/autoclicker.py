import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, Key

delay = 0.1
button = Button.left

start_stop = Key.f8
exit_key = Key.f7


class Clickmouse(threading.Thread):

    def __init__(self, delay, button):
        super(Clickmouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True

    def start_click(self):
        self.running = True

    def stop_click(self):
        self.running = False

    def exit(self):
        self.stop_click()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                mouse.click(self.button)
                time.sleep(self.delay)

            time.sleep(0.1)


mouse = Controller()
click_thread = Clickmouse(delay, button)
click_thread.start()


def on_press(key):
    if key == start_stop:
        if click_thread.running:
            click_thread.stop_click()

        else:
            click_thread.start_click()

    elif key == exit_key:
        click_thread.exit()
        listener.stop()


with Listener(on_press=on_press) as listener:
    listener.join()
