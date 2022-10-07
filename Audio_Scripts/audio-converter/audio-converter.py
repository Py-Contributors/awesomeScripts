import subprocess
import os
import argparse


parser = argparse.ArgumentParser(
    description='A program to convert audio to another audio format'
)
parser.add_argument(
    '-p',
    '--path',
    type=str,
    help='''
The full path of file to convert OR
the full path of folder that contains all files to convert'
    ''',
    required=True
)
parser.add_argument(
    '-e',
    '--extension',
    type=str,
    help='The type of extension to convert the audio',
    default='.mp3',
    required=False
)


def convert(file, extension):
    file_name, _ = file.split('.')
    output_name = file_name + extension
    subprocess.run(['ffmpeg', '-i', file, output_name])


def convert_all(path, extension):
    for _, _, files in os.walk(path):
        for file in files:
            convert(file, extension)


if __name__ == "__main__":
    args = parser.parse_args()
    path = args.path
    extension = args.extension

    os.chdir(os.path.dirname(path))

    if (os.path.isdir(path)):
        convert_all(path=path, extension=extension)
    else:
        convert(file=path, extension=extension)
