# DeadOrNot

PingChecker is a Python program that checks your latency for various games by pinging the game servers

## Getting Started

### Prerequisites
The following are needed to run DeadOrNot
* [Python/Python 3] (https://www.python.org/)

### Installation
```
1. Use [pip](https://pip.pypa.io/en/stable/) to install the requirements.
```bash
pip install -r requirements.txt
```

## Usage

Use the -h option to see information and other options
```bash
python pingChecker.py -h
```

Check and output game status using flags for respective games 
Currently supported games
-f or --fortnite for Fortnite
-d or --dota for Dota 2 
-l or -lol for League of Legends
-he or -heart for HearthStone
-ho or --hots for Heroes of the Storm
-w or --wow for World of Warcraft 
-s or -star for Starcraft 2
-o or -overwatch for Overwatch

```bash
python pingChecker.py --lol
```
Add argument to narrow down servers by region, region combinations are permitted, i.e using NA EU will show latency for both Europe and North America
Currently supported regions
All - for all regions - default
NA - for North America
EU - for Europe
OCE - for Oceania 
SA - for South America
MEA - for the Middle East 
Asia - for Asia
```bash
python pingChecker.py NA -lol
```

## Contributing
Any help, ideas or issues with the program are welcome and encouraged. 

## License
Distributed under the [MIT](https://choosealicense.com/licenses/mit/) License. See LICENSE for more information.
