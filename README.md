# YouTube video downloader for the terminal

YouTube video downloader written in python utilizing the [PyTube](https://pytube.io/en/latest/) library as well as the [argparse](https://docs.python.org/3/library/argparse.html) module for adding flags (currently only a help flag and an output path flag). It can be easily extended to fit your own needs.

## How to use?

You run it with `python3 yt_video_dl.py <YouTube video url> -o /path/to/output` or if you prefer compiling the file using PyInstaller, you can then compile the file like this `pyinstaller yt_video_dl.py -F` the -F flag means that it creates a single executable file in the `dist` directory. You then run the compiled file like this `./yt_video_dl <YouTube video url> -o /path/to/output` if no path is specified it will create folder called 'downloadedVideos' and download it there.
