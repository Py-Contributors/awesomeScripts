import sys
import datetime as dt


def clock():
    try:
        print("\n\tThe Time is \n")
        while(1):
            print("\r\t{}".format(dt.datetime.today()), end="")
    except KeyboardInterrupt:
        pass


def stopwatch():
    starttime = dt.datetime.now()
    print("\n\tStart Time: " + str(starttime))
    print("\n\tTime Taken\n")
    try:
        while(1):
            print("\r\t{}".format(dt.datetime.now() - starttime), end="")
    except KeyboardInterrupt:
        pass


def timer(op, time):
    stoptime = dt.timedelta()
    if op == '-s':
        stoptime = dt.timedelta(seconds=time)
    elif op == '-m':
        stoptime = dt.timedelta(minutes=time)
    else:
        raise IndexError
    try:
        starttime = dt.datetime.now()
        print("\n\tTime Left\n")
        while dt.datetime.now() - starttime != stopwatch:
            elapsed_time = dt.datetime.now() - starttime
            print("\r\t{}".format(stoptime - elapsed_time), end="")
    except KeyboardInterrupt:
        pass


def help():
    print("\n Clock Module")
    print("\n\t The following options are available")
    print("\n\t\t --clock\tTo display the digital clock. Use Ctrl+C to exit")
    print("\n\t\t --stopwatch\tTo start the stopwatch. Use Ctrl+C to exit")
    print("\n\t\t --timer With additional arguments")
    print("\n\t\t\t -s <number> To start timer for <number> seconds")
    print("\n\t\t\t -m <number> To start timer for <number> minutes")


if __name__ == "__main__":
    try:
        if sys.argv[1] == '--clock':
            clock()
        elif sys.argv[1] == '--stopwatch':
            stopwatch()
        elif sys.argv[1] == '--timer':
            timer(sys.argv[2], int(sys.argv[3]))
        else:
            help()
    except IndexError:
        help()
