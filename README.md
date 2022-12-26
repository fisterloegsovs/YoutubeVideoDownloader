# YouTube video downloader for the terminal

YouTube video downloader written in python utilizing the [PyTube](https://pytube.io/en/latest/) library as well as the [argparse](https://docs.python.org/3/library/argparse.html) module for adding flags (currently only a help flag and an output path flag). It can be easily extended to fit your own needs.

## Compiling the project to make an executable file

One can compile the python file using PyInstaller, which can be installed using pip3 with the command `pip3 install pyinstaller`.

This might be desirable if you wish to run the code many times as this will decrease run time, and also simplify the command to download the videos, at least a little bit :-).

## How to use?

You run it with `python3 yt_video_dl.py <YouTube video url> -o /path/to/output` or if you prefer compiling the file using PyInstaller, you can then compile the file like this `pyinstaller yt_video_dl.py -F` the -F flag means that it creates a single executable file in the `dist` directory. You then run the compiled file like this `./yt_video_dl <YouTube video url> -o /path/to/output`
