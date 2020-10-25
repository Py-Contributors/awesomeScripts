# Check Github username

This script allows verify if an username is available or not.

## Dependencies

Install Python in version 3 or later and the `requests` module using `pip`.

Example on Linux:
```sh
# on Debian
sudo apt-get install python
# on Arch Linux
sudo pacman -Sy python

# Installing dependencies
python3 -m pip install -r requirements.txt
```

## Usage

Start the script passing an username which you want to know about it avalability.

```
python CheckUsername.py <username>
```

Example:
```console
$ python CheckUsername.py pinho
Searching username "pinho"
Username is already in use :(
```

---

Made by [@pinho](https://github.com/pinho)
