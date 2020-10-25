import sys
import requests

API_URI = 'https://api.github.com/users'


def main(argv):
    u = argv[1]
    print(f'Searching username "{u}"')
    res = requests.get(f'{API_URI}/{u}')

    if res.status_code == 404:  # Not found
        print('Username is available :D', end='')
    else:
        print('Username is already in use :(', end='')
    # print(f' -- ({res.status_code})')
    print()


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Missing <username> parameter', file=sys.stderr)
        exit(1)
    else:
        main(sys.argv)
