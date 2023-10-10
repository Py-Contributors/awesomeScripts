# Ping Sweep Network Scanner

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Usage](#usage)
- [Example](#example)

## Overview

This Python script allows you to perform a ping sweep on a range of IP addresses within a specified subnet to identify live hosts. It supports both Windows and Unix-like systems for the ping command.

## Features

- Scan a range of IP addresses within a subnet.
- Detect live hosts within the specified range.
- Cross-platform compatibility (Windows and Unix-like systems).

## Usage

1. Run the program

   * For Windows (Powershell/CMD): 

      ```
      python main.py
      ```

   * For Linux (bash/zsh/unix):

      ```bash
      sudo python3 main.py
      ```

   `Root privilege is required for linux users, as modern kernels of linux don't allow pinging without root privilege.`

2. Follow the on-screen instructions to provide the following information:

   * Subnet IP (e.g., 192.168.0)
   * Starting IP range
   * Ending IP range

## Example

```
Enter the SUBNET IP: 192.168.1
Enter Starting Range: 1
Enter Ending Range: 10
```
The script will scan the hosts ranging from IP Address: 192.168.1.1 to 192.168.1.10.

```
Scanning completed in 0:00:13.741418

Live Hosts:
192.168.1.1 --> Live
192.168.1.2 --> Live
192.168.1.5 --> Live
192.168.1.7 --> Live
192.168.1.9 --> Live
```

---

`The efficiency of the program solely depends on factors such as network traffic and connectivity of devices to the router/dhcp server. Also, in some cases, the program skips some live hosts, even though they're up due to delay in responding to the ping command within the time slot.`
