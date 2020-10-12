import shutil
import argparse
import datetime
import time


def get_free_space(path):
    """
    Return the free space of the given path
    """
    _, _, free = shutil.disk_usage(path)
    return free


def get_free_space_hr(path):
    """
    Return the free space of the given path in a human readable format
    """
    free = get_free_space(path)
    hr_free = ''
    for unit, idx in zip(['k', 'M', 'G', 'T', 'P'], range(10, 50, 10)):
        hr_usage = (free % (2 ** (idx + 10))) // (2 ** idx)
        if hr_usage == 0:
            break
        hr_free = f"{hr_usage}{unit} {hr_free}"
    return hr_free


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Display and log the free disk space from a given folder')
    parser.add_argument('path', help="Path for using the disk usage", type=str)
    parser.add_argument('-n', '--interval',
                        help="Interval in seconds (default: 2)",
                        type=int, default=2)
    parser.add_argument('-f', '--logfile',
                        help="Path to logfile to log the disk usage",
                        type=str, default=None)
    parser.add_argument('-q', '--quite',
                        help="Quite mode: No output will be displayed",
                        action="store_true")
    args = parser.parse_args()
    while True:
        hr_free = get_free_space_hr(args.path)
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if not args.quite:
            print(f"{now} {hr_free}")
        if args.logfile:
            with open(args.logfile, 'a') as outfile:
                outfile.write(f"{now} {hr_free}\n")
        time.sleep(args.interval)
