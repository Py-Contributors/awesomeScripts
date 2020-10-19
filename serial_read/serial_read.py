# python Imports
import argparse
import signal    # Using this library to catch keyboard interrupts
import sys       # system library
import serial    # Python pyserial library !DOC -> https://pypi.org/project/pyserial/


def signal_handler(signal, frame):
    print('Keyboard Interrupt caught -> Exiting')
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)


def parse_command_line_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description=(
        'Example Serial Read Code.'))
    parser.add_argument(
        '--timeout',
        default=None,
        dest='timeout',
        type=float,
        help='Set a read timeout value.')
    parser.add_argument(
        '--bytesize',
        default=8,
        type=int,
        dest='bytesize',
        help="Number of data bits.")
    parser.add_argument(
        '--port',
        choices=("/dev/ttyUSB0", "COM3"),
        default="/dev/ttyUSB0",
        dest='port',
        help='PORT a device name.')
    parser.add_argument(
        '--baudrate',
        choices=(110, 300, 600, 1200, 2400, 4800, 9600, 14400,
                 19200, 38400, 57600, 115200, 128000, 256000),
        default=9600,
        type=int,
        dest='baudrate',
        help='Baud rate for serial Communication')

    return parser.parse_args()


def readInfiniteLoop():
    """This funtions reads from serial and prints it on console"""

    # pass command line arguments (if provided, otherwise default values are used) to variables
    arg = parse_command_line_args()
    print("Config : {}".format(arg))
    port = arg.port
    baudrate = arg.baudrate
    timeout = arg.timeout
    byteSize = arg.bytesize

    # init serial module
    serialRead = serial.Serial(
        port=port, baudrate=baudrate, bytesize=byteSize, timeout=timeout)
    while True:
        # Reads incoming data from serial into originalData
        originalData = serialRead.readline()
        # Convert byte data into standard "UTF-8" format
        stringData = originalData.decode('utf-8')
        # Slicing to remove /r and /n at the end (Line Feed and NewLine)
        stringData = stringData[:-2]
        print("Original Data (byte format): {}  | Filtered Data: {}".format(
            originalData, stringData))


if __name__ == "__main__":
    readInfiniteLoop()
