
# Serial Communication Using Python
----
## Features

- Read Serial Data

## Dependencies 

Follow following steps to install dependencies (Linux)

```bash
python3 -m pip install pyserial  #To install pyserial python module
```

## Usage

This directory contains an awesome script to read serial data from any device e.g. ``Arduino, Raspberry Pi, ESP32 or ESP8266, or even from a virtual serial port``. To Create virtual serial port in linux : [Serial Port Linux](https://tewarid.github.io/2015/04/07/virtual-serial-port-redirection-using-socat.html).


##### To check commandline argument help messages:

```bash
python3 serial_read.py -h
```
```
# output
usage: serial_read.py [-h] [--timeout TIMEOUT] [--bytesize BYTESIZE] [--port {/dev/ttyUSB0,COM3}] [--baudrate {110,300,600,1200,2400,4800,9600,14400,19200,38400,57600,115200,128000,256000}] {} ...

Example Serial Read Code.

positional arguments:
  {}

optional arguments:
  -h, --help            show this help message and exit
  --timeout TIMEOUT     Set a read timeout value.
  --bytesize BYTESIZE   Number of data bits.
  --port {/dev/ttyUSB0,COM3}
                        PORT a device name.
  --baudrate {110,300,600,1200,2400,4800,9600,14400,19200,38400,57600,115200,128000,256000}
                        Baud rate for serial Communication
```


##### You can run the script by typing :

```bash
python3 serial_read.py \
 --port="/dev/ttyUSB0" \
 --baudrate=9600 \
 --bytesize=8 #change arguments as per your requirement
```
##### Sample Output

###### Here, I am using ESP8266 as a serial module which is connected to Linux machine as "/dev/ttyUSB0"

```bash
Config : Namespace(baudrate=9600, bytesize=8, port='/dev/ttyUSB0', timeout=None)
Original Data (byte format): b'Sending this from ESP8266\r\n'  | Filtered Data: Sending this from ESP8266
Original Data (byte format): b'Sending this from ESP8266\r\n'  | Filtered Data: Sending this from ESP8266
Original Data (byte format): b'Sending this from ESP8266\r\n'  | Filtered Data: Sending this from ESP8266
Original Data (byte format): b'Sending this from ESP8266\r\n'  | Filtered Data: Sending this from ESP8266
...
...
...
^CKeyboard Interrupt caught -> Exiting
```