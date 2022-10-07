# Pomodoro Timer

## Description
Improve you work flow by doing a list of tasks in 25 minute intervals with short and long breaks in between

### Timer Defaults
- Focus time : 25 minutes
- Long breaks: 20 minutes
- Short break: 5 minutes

### Timer Flow
Start
- Timer starts with default 25 minute focus time
- Short break starts after 1st and 3rd focus sessions
- Long break starts after 2nd focus session

Reset
- Timer can be reset at anytime during the session 
- Timer resets to default focus time

## Requirements
- MacOS
- Tkinter
  - To install tkinter follow these instructions
  https://www.geeksforgeeks.org/how-to-install-tkinter-on-macos/ 
- tkmacosx
  - To install tkmacosx run this in terminal
  ```sh
    pip3 install tkmacosx
    ```

## Other Notes
### How to change timer constants
1. Locate pomodoro_timer_gui.py
2. Under the comment header 'GLOBAL CONSTANTS', find the comment 'timer constants'
3. Enter preferred values
4. Save and run
> NOTE: Potential added feature in User Interface