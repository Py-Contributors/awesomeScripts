# yt_clipper

**This script is currently maintained at: https://github.com/epassaro/yt_clipper**

Easily make audio/video/gif clips from YouTube URLs.

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
usage: yt_clipper [-h] [-d DEVICE] [-u VALUE] [-x {fast,medium,slow}] [-s SIZE] [-c {aac,mp3}] [-b {96k,128k,192k,256k,320k}] [-a] [-g] [-f FPS] [-o FILENAME] [-q]
                  url start end

easily make audio/video/gif clips from YouTube URLs

positional arguments:
  url                             video url
  start                           HH:MM:SS.ms
  end                             HH:MM:SS.ms

optional arguments:
  -h, --help                      show this help message and exit
  -d DEVICE, --device DEVICE      VA-API hardware acceleration device (experimental), for example: '/dev/dri/render128D'
  -u VALUE, --quality VALUE       from 0 to 51, default is 23 (lower is better)
  -x {fast,medium,slow}, --compression {fast,medium,slow}
                                  encoder preset (cpu only)
  -s SIZE, --scale SIZE           scale image vertically (in px)
  -c {aac,mp3}, --audio-codec {aac,mp3}
  -b {96k,128k,192k,256k,320k}, --bitrate {96k,128k,192k,256k,320k}
                                  audio constant bitrate (CBR)
  -a, --audio-only
  -g, --gif
  -f FPS, --fps FPS               gif fps
  -o FILENAME, --output FILENAME  custom file name and container
  -q, --quiet

```

