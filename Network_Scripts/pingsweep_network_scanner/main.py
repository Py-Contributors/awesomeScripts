import functions


def main():
    live_hosts = functions.network_scan()
    if live_hosts:
        print("\nLive Hosts:")
        for host, status in live_hosts:
            print(f"{host} --> {status}")
    else:
        print("\nNo devices up and running in the given range of network.")


if __name__ == "__main__":
    functions.instructions()
    main()
