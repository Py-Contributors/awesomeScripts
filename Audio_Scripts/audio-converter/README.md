# Audio Converter

CLI tool to convert an audio file from one extension to another (e.g. mp3 to wav)

## Requirements
- [FFmpeg](https://ffmpeg.org/)

## Usage

### Convert all audio files in a specific directory
```bash
python3 audio-converter.py -p <YOUR-PATH-WAS-HERE> -e <THE-DESIRED-EXTENSION>
```

e.g.
```bash
python3 audio-converter.py -p /home/username/Music -e .wav
```

### Convert specific audio file
```bash
python3 audio-converter.py -p <YOUR-PATH-WAS-HERE> -e <THE-DESIRED-EXTENSION>
```

e.g.
```bash
python3 audio-converter.py -p /home/username/Music/test.mp3 -e .wav
```
