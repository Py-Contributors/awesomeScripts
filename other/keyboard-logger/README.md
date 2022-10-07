# Keyboard Logger
A Python script that logs input from the keyboard.
## Features
- Appends the input keys to a log file - 'keyboard.log' (unless otherwise specified), in the format TIMESTAMP : KEY(s)_PRESSED.
- For better readability of the log file, a new timestamp is added only when:
    - A special key (non-alphanumeric) is pressed.
    - It has been greater than 2 seconds since the lastest key press. 
- Hotkey detection will be added in the near-future
## Usage
`python3 keyboard-logger.py` (OR)
`python3 keyboard-logger.py filename.log`
