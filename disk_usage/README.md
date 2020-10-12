Display and/log the free space of a given path every N seconds. 

usage: disk_usage.py [-h] [-n INTERVAL] [-f LOGFILE] [-q] path

Display and log the free disk space from a given folder

positional arguments:
  path                  Path for using the disk usage

optional arguments:
  -h, --help            show this help message and exit
  -n INTERVAL, --interval INTERVAL
                        Interval in seconds (default: 2)
  -f LOGFILE, --logfile LOGFILE
                        Path to logfile to log the disk usage
  -q, --quite           Quite mode: No output will be displayed
