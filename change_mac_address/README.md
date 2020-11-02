### A Script to change the MAC address

This script changes the MAC address of the selected interface/device using `ifconfig`. Make sure 
`ifconfig` is installed on your pc.

---

####  Install on Debian

```
apt-get install net-tools
```

#### Install on Arch Linux

```
pacman -S net-tools
```

### usage

- for help:

```python
sudo python mac_address_changer.py -h 
```

```python
sudo python mac_address_changer.py <nameofinterface> <macaddress>
```
