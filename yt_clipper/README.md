# yt_clipper

This script is intended to be used with `python>=3.6`.

## Installation

First of all, install `youtube-dl` with `pip`:

```
pip install --upgrade youtube-dl --user
```

Also you will need `ffmpeg` installed on your system.

**On Debian-based distros:**

```
$ sudo apt install ffmpeg
```

**On macOS:**

```
$ brew install ffmpeg
```

## Usage

```
usage: yt_clipper.py [-h] [-s SCALE] [-a] [-g] [-f FPS] [-o OUTPUT] [-q]
                     url start end

make clips from youtube videos

positional arguments:
  url                           video url
  start                         HH:MM:SS
  end                           HH:MM:SS

optional arguments:
  -h, --help                    show this help message and exit
  -s SCALE, --scale SCALE       scale image vertically (in px)
  -a, --audio-only
  -g, --gif
  -f FPS, --fps FPS             gif fps
  -o OUTPUT, --output OUTPUT
  -q, --quiet
```
