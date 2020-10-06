import speedtest as st


def speedtest():
    """Runs a speedtest on your internet connection"""
    try:
        res = st.Speedtest()
    except st.ConfigRetrievalError:
        return "Not connected to internet"

    # Create a spinner on command line to show that its running
    print('Running the test ')

    res.get_best_server()
    download_speed = res.download()
    upload_speed = res.upload()

    # Print the results
    print('Speed test results:')
    print('Download: ' + pretty_speed(download_speed))
    print('Upload: ' + pretty_speed(upload_speed))


def pretty_speed(speed):
    """
    return speed value prettily accordingly in either bps, Kbps, Mbps, Gbps
    """
    unit = 'bps'
    kmg = ['', 'K', 'M', 'G']
    i = 0
    while speed >= 1000:
        speed /= 1000
        i += 1
    return "{:.2f}".format(speed) + ' ' + kmg[i] + unit


speedtest()
