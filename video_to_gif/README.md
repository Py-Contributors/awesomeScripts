## Video 2 GIF

The script converts videos to GIFs.


## Setup

Install the packages listed in `requirements.txt` using `pip`

```bash
pip install -r requirements.txt
```

## Usage

```bash
cd video_to_gif
python3 video2gif.py <path-to-file> --start <time-in-seconds> --end <time-in-seconds>
```

The following script created 'falkirk_wheel.gif', which loopes from 2 to 6 seconds.
```
python3 video2gif.py ./falkirk_wheel.webm --start 2 --end 6
```