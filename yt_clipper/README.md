# yt_clipper

Easily make audio/video/gif clips from YouTube URLs with ffmpeg.

## Installation

This script is intended to be used with `python>=3.6` and with any Linux distribution.
However, the script should work on other platforms.

First of all, install `youtube-dl` with `pip`:

```
pip install --upgrade youtube-dl --user
```

Also you will need `ffmpeg` installed on your system. To use VA-API hardware acceleration
you will need a `ffmpeg` version compiled with VA-API flags enabled.

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
usage: yt_clipper [-h] [-d DEVICE] [-s SCALE] [-a] [-g] [-f FPS] [-o OUTPUT] [-q] url start end

easily make audio/video/gif clips from YouTube URLs with ffmpeg

positional arguments:
  url                           video url
  start                         HH:MM:SS.ms
  end                           HH:MM:SS.ms

optional arguments:
  -h, --help                    show this help message and exit
  -d DEVICE, --device DEVICE    device for VAAPI hardware acceleration (experimental), for example: '/dev/dri/render128D'
  -s SCALE, --scale SCALE       scale image vertically (in px)
  -a, --audio-only
  -g, --gif
  -f FPS, --fps FPS             gif fps
  -o OUTPUT, --output OUTPUT
  -q, --quiet

```

