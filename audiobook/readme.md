# Audio Book

> Read any PDF book with just few line of

## Installation

Create new Virtual ENV:

```sh
pip install pipenv
pipenv install -r requirements.txt
pipenv shell
```

you can also download the audiobook module with help of pip

```bash
pip install audiobook
```

## Usage example

Audio Book is Python script to read pdf files.Use command link to enter the file location

```sh
python3 read_my_book.py <book_path>
```

### Linux installation requirements

- If you are on a linux system and if the voice output is not working , then :
    Install espeak , ffmpeg and libespeak1 as shown below:

```sh
sudo apt update && sudo apt install espeak ffmpeg libespeak1
```

documentation:- <https://github.com/nateshmbhat/pyttsx3>
