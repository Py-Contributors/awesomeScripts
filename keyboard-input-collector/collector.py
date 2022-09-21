from pynput.keyboard import Key, Listener


def on_press(key):
    print(f'{key} pressed')

    if key == Key.esc:
        return False 
        # When esc is clicked finish logging

if __name__ == '__main__':
    with Listener(
            on_press=on_press) as listener:
        listener.join()
        # Adding an event listener
