from moviepy.editor import VideoFileClip
import re
import argparse


def video_to_gif(PATH, START_TIME, END_TIME, OUTPUT_NAME):

    if not START_TIME or not END_TIME:
        clip = VideoFileClip(PATH)
    else:
        print("Creating GIF from time %s sec to %s sec." % (str(START_TIME), str(END_TIME)))
        clip = VideoFileClip(PATH).subclip((START_TIME), (END_TIME))
    clip.write_gif(OUTPUT_NAME)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="Path of video file")
    parser.add_argument("--start", "-s", help="Start time")
    parser.add_argument("--end", "-e", help="End time")
    args = parser.parse_args()
    PATH = args.path
    START_TIME = args.start
    END_TIME = args.end
    VIDEO_EXT = re.search(r"\.([a-zA-Z0-9]{2,5}$)", PATH).group(1)
    OUTPUT_NAME = PATH.replace(VIDEO_EXT, "gif", 1)
    video_to_gif(PATH, START_TIME, END_TIME, OUTPUT_NAME)


if __name__ == "__main__":
    main()
