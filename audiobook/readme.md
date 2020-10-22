# Audio Book

> Listen any PDF book with just few line of

## Installation

Install the audibook with pip

```sh
pip install audiobook
```

## Usage example

Audio Book is Python script to read pdf files.Use command link to enter the file location

```python

from audiobook import Audiobook
ab = Audiobook("file_path")
ab.text_to_speech()
```

### Linux installation requirements

- If you are on a linux system and if the voice output is not working , then :
    Install espeak , ffmpeg and libespeak1 as shown below:

```sh
sudo apt update && sudo apt install espeak ffmpeg libespeak1
```

documentation:- <https://github.com/nateshmbhat/pyttsx3>
