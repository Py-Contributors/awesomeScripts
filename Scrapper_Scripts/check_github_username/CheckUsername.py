import sys
import requests
import argparse

arg = argparse.ArgumentParser()
arg.add_argument('-u', '--username', help='Username to check')
args = arg.parse_args()

API_URI = 'https://api.github.com/users'

def check_username_available(username: str):
    print('Searching username {}'.format(username))
    res = requests.get('{}/{}'.format(API_URI, username))

    if res.status_code == 404:  # Not found
        return True
    elif res.status_code == 200:
        return False
    else:
        raise Exception('Error: {}'.format(res.status_code))


if __name__ == '__main__':
    username = args.username
    output = check_username_available(username)
    if output:
        print('Username is available :)', end='')
    else:
        print('Username is already in use :(', end='')
        
    
    
