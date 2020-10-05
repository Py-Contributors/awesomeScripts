# Title - Open map location using CLI

# importing all the required libraries
import webbrowser
import sys

# It returns the list of the commandline arguments
sys.argv

# It checks whether the location is provided or not
if(len(sys.argv) > 1):
    addr = ''.join(sys.argv[1:])

# It opens the location specified in the browser
webbrowser.open('https://www.google.com/maps/place/' + addr)
